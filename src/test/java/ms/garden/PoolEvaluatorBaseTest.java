package ms.garden;

import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.function.Consumer;

import static java.util.Arrays.stream;
import static java.util.stream.Collectors.toList;
import static ms.garden.Point.point;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

public abstract class PoolEvaluatorBaseTest {

    protected PoolEvaluator evaluator = createPoolEvaluator();

    protected abstract PoolEvaluator createPoolEvaluator();

    @Test
    public void shouldFindIfPoolWillBeCreated() {
        Garden garden = new Garden(createGardenMap("" +
                "3 4 5 2 \n" +
                "1 0 3 4 \n" +
                "6 7 8 2 \n" +
                "1 3 2 3 \n" +
                "7 2 6 2"
        ));

        boolean[][] poolMap = createPoolMap("" +
                "+ + + - \n" +
                "+ + + + \n" +
                "+ + + - \n" +
                "- + + + \n" +
                "- - + -"
        );

        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated1() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 \n" +
                "8 8 1 8 8 \n" +
                "8 1 1 1 8 \n" +
                "8 8 1 8 8 \n" +
                "8 8 1 8 8"
        ));

        boolean[][] poolMap = createPoolMap("" +
                "- - - - - \n" +
                "- - - - - \n" +
                "- - - - - \n" +
                "- - - - - \n" +
                "- - - - - "
        );

        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated2() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 \n" +
                "8 8 1 8 8 \n" +
                "8 1 4 1 8 \n" +
                "8 8 1 8 8 \n" +
                "8 8 1 8 8"
        ));

        boolean[][] poolMap = createPoolMap("" +
                "+ + + + + \n" +
                "+ + + + + \n" +
                "+ + + + + \n" +
                "+ + - + + \n" +
                "+ + - + + "
        );


        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated3() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 8 \n" +
                "8 4 4 4 8 8 \n" +
                "8 4 5 4 8 8 \n" +
                "8 4 3 3 8 8 \n" +
                "8 8 8 3 2 2 \n" +
                "8 8 8 2 1 2 \n" +
                "8 8 8 2 2 2 "
        ));

        boolean[][] poolMap = createPoolMap("" +
                "+ + + + + + \n" +
                "+ + + + + + \n" +
                "+ + + + + + \n" +
                "+ + + + + + \n" +
                "+ + + + + + \n" +
                "+ + + + + + \n" +
                "+ + + + + + "
        );


        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated4() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 8 \n" +
                "8 4 4 4 8 8 \n" +
                "8 4 5 4 8 8 \n" +
                "8 4 3 3 8 8 \n" +
                "8 8 8 3 2 2 \n" +
                "8 8 8 2 1 1 \n" +
                "8 8 8 2 2 2 "
        ));

        boolean[][] poolMap = createPoolMap("" +
                "- - - - - - \n" +
                "- - - - - - \n" +
                "- - - - - - \n" +
                "- - - - - - \n" +
                "- - - - - - \n" +
                "- - - - - - \n" +
                "- - - - - - "
        );


        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated5() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 8 8 8 8 8 8 \n" +
                "8 1 1 2 2 2 1 8 8 8 8 \n" +
                "8 1 8 8 3 8 1 1 1 1 8 \n" +
                "8 1 2 3 4 3 2 1 8 1 8 \n" +
                "8 1 8 8 3 8 2 1 8 1 8 \n" +
                "8 1 8 8 2 8 8 1 8 1 8 \n" +
                "8 1 1 2 2 2 1 1 1 1 8 \n" +
                "8 8 1 1 2 1 1 8 8 8 8 \n" +
                "8 8 8 1 2 2 1 8 8 8 8 "
        ));

        boolean[][] poolMap = createPoolMap("" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - \n" +
                "- - - - - - - - - - - "
        );


        assertPoolMapMatches(garden, poolMap);
    }

    @Test
    public void shouldFindIfComplexPoolWillBeCreated6() {
        Garden garden = new Garden(createGardenMap("" +
                "8 8 8 8 8 8 8 8 8 8 8 \n" +
                "8 1 1 2 2 2 1 8 8 8 8 \n" +
                "8 1 8 8 3 8 1 1 1 1 8 \n" +
                "8 1 2 3 4 3 2 1 8 1 8 \n" +
                "8 1 8 8 3 8 2 1 8 1 8 \n" +
                "8 1 8 8 2 8 8 1 8 1 8 \n" +
                "8 1 1 2 2 2 1 1 1 1 8 \n" +
                "8 8 1 1 2 1 1 8 8 8 8 \n" +
                "8 8 8 2 2 2 1 8 8 8 8 "
        ));

        boolean[][] poolMap = createPoolMap("" +
                "+ + + + + + + + + + + \n" +
                "+ + + + + + - + + + + \n" +
                "+ + + + + + - - - - + \n" +
                "+ + + + + - - - - - + \n" +
                "+ + + + + + - - - - + \n" +
                "+ + + + + + + - - - + \n" +
                "+ + + + + + - - - - + \n" +
                "+ + + + + - - + + + + \n" +
                "+ + + + + + - + + + + "
        );


        assertPoolMapMatches(garden, poolMap);
    }


    private void assertPoolMapMatches(Garden garden, boolean[][] poolMap) {
        forEachPointOn(garden, point -> {
            assertThat("wrong pool evaluation for " + point, evaluator.createsPoolIfRainingOnPoint(garden, point), equalTo(poolMap[point.y][point.x]));
        });
    }


    private int[][] createGardenMap(String gardenMap) {
        List<int[]> rows = stream(gardenMap.split("\n"))
                .map(row -> {
                    String[] parts = row.trim().split(" ");
                    int array[] = new int[parts.length];
                    for (int i = 0; i < parts.length; i++) {
                        array[i] = Integer.parseInt(parts[i]);
                    }
                    return array;
                }).collect(toList());
        int map[][] = new int[rows.size()][];
        for (int i = 0; i < rows.size(); i++) {
            map[i] = rows.get(i);
        }
        return map;
    }

    private boolean[][] createPoolMap(String poolMap) {
        List<boolean[]> rows = stream(poolMap.split("\n"))
                .map(row -> {
                    String[] parts = row.trim().split(" ");
                    boolean array[] = new boolean[parts.length];
                    for (int i = 0; i < parts.length; i++) {
                        array[i] = "+".equals(parts[i]);
                    }
                    return array;
                }).collect(toList());
        boolean map[][] = new boolean[rows.size()][];
        for (int i = 0; i < rows.size(); i++) {
            map[i] = rows.get(i);
        }
        return map;
    }

    private void forEachPointOn(Garden garden, Consumer<Point> pointAssertion) {
        for (int x = 0; x < garden.getWidth(); x++) {
            for (int y = 0; y < garden.getHeight(); y++) {
                Point point = point(x, y);
                pointAssertion.accept(point);
            }
        }
    }
}