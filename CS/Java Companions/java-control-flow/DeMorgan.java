public class DeMorgan {
    // Pads "true" to the width of "false" so that the columns line up.
    public static String cell(boolean value) {
        if (value) {
            return "true    ";
        }
        return "false   ";
    }

    public static void main(String[] args) {
        System.out.println("a       b       | !(a&&b) !a||!b  | !(a||b) !a&&!b");
        for (int i = 1; i >= 0; i--) {
            for (int j = 1; j >= 0; j--) {
                boolean a = (i == 1);
                boolean b = (j == 1);
                System.out.println(cell(a) + cell(b) + "| " + cell(!(a && b)) + cell(!a || !b) + "| " + cell(!(a || b)) + cell(!a && !b));
            }
        }

        int age = 15;
        boolean hasTicket = true;
        System.out.println(!(age >= 18 && hasTicket));
        System.out.println(age < 18 || !hasTicket);      // the same test with the ! pushed inside
    }
}
