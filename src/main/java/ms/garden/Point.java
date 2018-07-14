package ms.garden;

import javafixes.object.DataObject;

import java.util.Set;

import static javafixes.common.CollectionUtil.newLinkedSet;

public class Point extends DataObject {

    public final int x;
    public final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static Point point(int x, int y) {
        return new Point(x, y);
    }

    public Point pointOnLeft() {
        return new Point(x - 1, y);
    }

    public Point pointOnRight() {
        return new Point(x + 1, y);
    }

    public Point pointAbove() {
        return new Point(x, y - 1);
    }

    public Point pointBellow() {
        return new Point(x, y + 1);
    }

    public Set<Point> neighbouringPoints() {
        return newLinkedSet(pointOnLeft(), pointAbove(), pointOnRight(), pointBellow());
    }
}
