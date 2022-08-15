package vm.teacher;

import javax.swing.*;
import java.awt.*;


public class ColorViewer extends JFrame {

    public ColorViewer(Iterable<Color> colorsProvider) {

        setTitle("Color Viewer");

        add(new JScrollPane(new ProjectionComponent(
                colorsProvider, 1280, 768, 1
        )));

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);
    }
}
