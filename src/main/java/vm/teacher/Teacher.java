package vm.teacher;

import vm.teacher.iterator.MappableIterable;

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

public class Teacher {

    public static void main(String[] args) {

        Iterable<Color> colorsProvider;

        File file = new File("c:/Windows/notepad.exe");

        try {
            List<Byte> content = toList(Files.readAllBytes(file.toPath()));

            colorsProvider = MappableIterable
                    .wrap(toList(toByteArray(content.size())))
                    .attach(content)
                    .flatMap(b -> toBooleanList(b))
                    .map(bool -> bool ? 255 : 0)
                    .aggregate(3, ints -> {
                        int r = ints.get(0);
                        int g = ints.size() > 1 ? ints.get(1) : 0;
                        int b = ints.size() > 2 ? ints.get(2) : 0;
                        return new Color(r, g, b);
                    }, false);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        SwingUtilities.invokeLater(() -> {
            ColorViewer teacher = new ColorViewer(colorsProvider);
            teacher.setVisible(true);
        });
    }

    private static List<Byte> toList(byte[] bytesArray) {
        List<Byte> bytes = new ArrayList<>();
        for (byte b : bytesArray) {
            bytes.add(b);
        }
        return bytes;
    }

    private static byte[] toByteArray(long value) {
        return ByteBuffer.allocate(8).putLong(value).array();
    }

    private static int toInt(byte b) {
        return (((int) b) << 24) >>> 24;
    }

    private static List<Boolean> toBooleanList(byte b) {
//        System.out.println(toInt(b));
        BitSet bitSet = BitSet.valueOf(new byte[]{b});
        List<Boolean> bits = new ArrayList<>();
//        System.out.print("- ");
        for (int i = 7; i >= 0; i--) {
            boolean bool = bitSet.get(i);
            bits.add(bool);
//            System.out.print((bool ? 1 : 0));
        }
//        System.out.println();
        return bits;
    }
}
