package vm.teacher.iterator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.function.Function;

public interface MappableIterator<T> extends Iterator<T> {

    static <T> MappableIterator<T> wrap(Iterator<T> iterator) {
        return new MappableIterator<T>() {
            @Override
            public boolean hasNext() {
                return iterator.hasNext();
            }

            @Override
            public T next() {
                return iterator.next();
            }
        };
    }

    default <T2> MappableIterator<T2> map(Function<T, T2> mapper) {
        return new MappableIterator<T2>() {
            @Override
            public boolean hasNext() {
                return MappableIterator.this.hasNext();
            }

            @Override
            public T2 next() {
                return mapper.apply(MappableIterator.this.next());
            }
        };
    }

    default <T2> MappableIterator<T2> flatMap(Function<T, Iterable<T2>> mapper) {
        return new MappableIterator<T2>() {

            private Iterator<T2> activeIterator;

            @Override
            public boolean hasNext() {
                ensureActiveIterator();
                return activeIterator.hasNext();
            }

            @Override
            public T2 next() {
                ensureActiveIterator();
                return activeIterator.next();
            }

            private void ensureActiveIterator() {
                while ((activeIterator == null || !activeIterator.hasNext()) && MappableIterator.this.hasNext()) {
                    activeIterator = mapper.apply(MappableIterator.this.next()).iterator();
                }
            }
        };
    }

    default MappableIterator<T> attach(Iterator<T> iterator) {
        return new MappableIterator<T>() {
            @Override
            public boolean hasNext() {
                return MappableIterator.this.hasNext() || iterator.hasNext();
            }

            @Override
            public T next() {
                return MappableIterator.this.hasNext() ? MappableIterator.this.next() : iterator.next();
            }
        };
    }

    default <T2> MappableIterator<T2> aggregate(int numberOfItems, Function<List<T>, T2> mapper, boolean allItemsRequired) {
        return new MappableIterator<T2>() {

            private List<T> itemsToAggregate;

            @Override
            public boolean hasNext() {
                fetchNextNItems();
                return itemsToAggregate.size() > 0 && (numberOfItems == itemsToAggregate.size() || !allItemsRequired);
            }

            @Override
            public T2 next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                T2 response = mapper.apply(itemsToAggregate);
                itemsToAggregate = null;
                return response;
            }

            public void fetchNextNItems() {
                if (itemsToAggregate == null) {
                    List<T> tempList = new ArrayList<>();
                    for (int i = 0; i < numberOfItems; i++) {
                        if (!MappableIterator.this.hasNext()) {
                            break;
                        }
                        tempList.add(MappableIterator.this.next());
                    }
                    itemsToAggregate = tempList;
                }
            }
        };
    }
}
