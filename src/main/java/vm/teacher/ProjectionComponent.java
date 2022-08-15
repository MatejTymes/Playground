package vm.teacher;

import vm.shred.Colors;

import javax.swing.*;
import java.awt.*;
import java.util.Iterator;

public class ProjectionComponent extends JComponent {

    private final Iterable<Color> colorIterable;
    private final int width;
    private final int height;
    private final int scalingFactor;

    public ProjectionComponent(Iterable<Color> colorIterable, int width, int height, int scalingFactor) {
        this.colorIterable = colorIterable;
        this.width = width;
        this.height = height;
        this.scalingFactor = scalingFactor;
    }

    public ProjectionComponent(Iterable<Color> colorIterable, int width, int height) {
        this(colorIterable, width, height, 1);
    }

    private void doDrawing(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        int descaledWidth = width / scalingFactor;
        int descaledHeight = height / scalingFactor;

        g2d.setColor(Color.WHITE);
        g2d.fillRect(0, 0, width, height);

        g2d.setColor(Colors.BORDER_COLOR);
        g2d.fillRect(0, 0, descaledWidth * scalingFactor, scalingFactor);
        g2d.fillRect(0, 0, scalingFactor, descaledHeight * scalingFactor);
        g2d.fillRect(0, (descaledHeight - 1) * scalingFactor, descaledWidth * scalingFactor, scalingFactor);
        g2d.fillRect((descaledWidth - 1) * scalingFactor, 0, scalingFactor, descaledHeight * scalingFactor);

        Iterator<Color> colorIterator = colorIterable.iterator();
        outer:
        for (int y = 1; y < descaledHeight - 1; y++) {
            for (int x = 1; x < descaledWidth - 1; x++) {
                if (!colorIterator.hasNext()) {
                    break outer;
                }

                g2d.setColor(colorIterator.next());
                g2d.fillRect(x * scalingFactor, y * scalingFactor, scalingFactor, scalingFactor);
            }
        }
    }

    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        doDrawing(g);
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(width, height);
    }

}