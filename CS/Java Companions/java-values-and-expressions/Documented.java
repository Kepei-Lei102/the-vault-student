/* Documented.java — the three kinds of comment, a precondition and a postcondition (AP CSA 1.8). */
public class Documented {

    /**
     * Returns the number of whole boxes needed to pack all the items.
     * Precondition:  items >= 0 and perBox > 0.
     * Postcondition: the value returned times perBox is at least items.
     */
    public static int boxesNeeded(int items, int perBox) {
        return (items + perBox - 1) / perBox;   // int division, rounded UP
    }

    public static void main(String[] args) {
        // a one-line comment
        /* a block comment
           can run over several lines */
        System.out.println(boxesNeeded(10, 4));
        System.out.println(boxesNeeded(12, 4));
        System.out.println(boxesNeeded(0, 4));
        System.out.println(boxesNeeded(10, 0));  // breaks the precondition: nobody checks for you
    }
}
