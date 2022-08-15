package vm.teacher.iterator;

import java.util.List;
import java.util.function.Function;

import static java.util.Arrays.asList;

public interface MappableIterable<T> extends Iterable<T> {

    @Override
    MappableIterator<T> iterator();

    static <T> MappableIterable<T> wrap(Iterable<T> iterable) {
        return () -> MappableIterator.wrap(iterable.iterator());
    }

    static <T> MappableIterable<T> emptyIterable(Class<T> typeClass) {
        return wrap(asList());
    }

    default <T2> MappableIterable<T2> map(Function<T, T2> mapper) {
        return () -> this.iterator().map(mapper);
    }

    default <T2> MappableIterable<T2> flatMap(Function<T, Iterable<T2>> mapper) {
        return () -> this.iterator().flatMap(mapper);
    }

    default MappableIterable<T> attach(Iterable<T> iterable) {
        return () -> this.iterator().attach(iterable.iterator());
    }

    default <T2> MappableIterable<T2> aggregate(int numberOfItems, Function<List<T>, T2> mapper, boolean allItemsRequired) {
        return () -> this.iterator().aggregate(numberOfItems, mapper, allItemsRequired);
    }
}
