import java.io.File;                         // File and IOException live in java.io
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class ReadFile {
    public static void main(String[] args) throws IOException {        // "if the file cannot be opened, stop"
        File f = new File("marks.txt");
        Scanner in = new Scanner(f);                                   // the same Scanner class as for the keyboard
        ArrayList<String> names = new ArrayList<String>();
        int total = 0;
        while (in.hasNext()) {                                         // is there anything left to read?
            String name = in.next();                                   // the next word
            int mark = in.nextInt();                                   // the next int
            names.add(name);
            total += mark;
        }
        in.close();
        System.out.println(names + " total " + total);

        Scanner lines = new Scanner(new File("marks.txt"));
        while (lines.hasNext()) {
            String line = lines.nextLine();                            // a whole line ...
            String[] parts = line.split(" ");                          // ... cut at the spaces into a String array
            System.out.print(parts[0].substring(0, 1) + parts[1] + " ");
        }
        lines.close();
        System.out.println();

        Scanner missing = new Scanner(new File("no-such-file.txt"));   // the program stops here with an exception
    }
}
