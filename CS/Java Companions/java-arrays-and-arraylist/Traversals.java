public class Traversals {
    public static void main(String[] args) {
        int[] temps = {18, 21, 19, 25};

        for (int i = 0; i < temps.length; i++) {     // indexed: you know WHERE you are
            System.out.print(i + ":" + temps[i] + " ");
        }
        System.out.println();

        for (int t : temps) {                        // enhanced for: "for each t in temps"; t is a COPY of the element
            System.out.print(t + " ");
        }
        System.out.println();

        for (int t : temps) {
            t = 0;                                   // changes the copy only
        }
        System.out.println(temps[0] + " " + temps[3]);

        for (int i = 0; i < temps.length; i++) {
            temps[i] = 0;                            // changes the array
        }
        System.out.println(temps[0] + " " + temps[3]);

        Tally[] tallies = {new Tally(1), new Tally(5)};
        for (Tally t : tallies) {
            t.bump();                                // t is a copy of the REFERENCE, so the object it points at changes
        }
        System.out.println(tallies[0] + " " + tallies[1]);
        for (Tally t : tallies) {
            t = new Tally(100);                      // re-points the copy; the array still holds the old objects
        }
        System.out.println(tallies[0] + " " + tallies[1]);
    }
}
