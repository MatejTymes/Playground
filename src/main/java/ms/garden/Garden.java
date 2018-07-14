package ms.garden;

import java.util.Collection;
import java.util.Set;

import static java.util.stream.Collectors.toList;
import static javafixes.common.CollectionUtil.newSet;

public class Garden {
    private final int[][] map;

    public Garden(int[][] map) {
        // todo: clone the map
        // todo: check the map is of rectangular shape

        this.map = map;
    }

    public int getWidth() {
        return map[0].length;
    }

    public int getHeight() {
        return map.length;
    }

    public int getPointHeight(Point point) {
        return map[point.y][point.x];
    }

    public boolean isOnMap(Point point) {
        return point.x >= 0 &&
                point.y >= 0 &&
                point.y < map.length &&
                point.x < map[point.y].length;
    }
}
