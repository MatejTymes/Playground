package ms.garden;

import com.google.common.base.Preconditions;

import java.util.Collection;
import java.util.Set;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static java.util.stream.Collectors.toList;
import static javafixes.common.CollectionUtil.newSet;

public class Garden {
    private final int[][] map;

    public Garden(int[][] map) {
        checkNotNull(map, "map can't be null");
        checkArgument(map.length > 0, "map can't be empty");

        int rowSize = map[0].length;
        int mapCopy[][] = new int[map.length][];
        for (int i = 0; i < map.length; i++) {
            checkArgument(map[i].length > 0, "row map[" + i + "] can't be empty");
            checkArgument(map[i].length == rowSize, "map isn't of a rectangular shape");

            mapCopy[i] = new int[map[i].length];
            System.arraycopy(map[i], 0, mapCopy[i], 0, map[i].length);
        }

        this.map = mapCopy;
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
