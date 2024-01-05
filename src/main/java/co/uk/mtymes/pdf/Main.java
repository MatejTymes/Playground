package co.uk.mtymes.pdf;

import org.apache.pdfbox.Loader;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageTree;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

public class Main {

    public static void main(String[] args) throws IOException {

        System.setProperty("file.encoding", "utf-8");

        var folderPath = "C:\\mtymes\\zdrojaky\\project\\GitHub\\Playground\\data\\";

//        var fileName = "512670608.pdf";
        var fileName = "Pohyby_4819084001_202309190629.pdf";
//        var fileName = "RB_potvrzeni_20230915150712.pdf";

        var pdfFile = new File(folderPath, fileName);

        PDDocument document = Loader.loadPDF(pdfFile);
        PDPageTree pages = document.getPages();

        PDFTextStripper textStripper = new PDFTextStripper();

        textStripper.setSortByPosition(true);
        textStripper.setStartPage(1);
        textStripper.setEndPage(pages.getCount());

        String text = textStripper.getText(document);
        System.out.println("*********************");
        System.out.println(text);
        System.out.println("*********************");

        try (OutputStreamWriter writer = new OutputStreamWriter(
                new FileOutputStream(new File(folderPath, fileName + ".txt")),
                StandardCharsets.UTF_8
        )) {
            writer.write(text, 0, text.length());
        }

//        for (PDPage page : pages) {
//            page.getContents()
//        }
//
//        var numberOfPages = document.getNumberOfPages();
//
//        System.out.println("numberOfPages = " + numberOfPages);
    }
}