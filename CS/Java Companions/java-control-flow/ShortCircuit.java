public class ShortCircuit {
    public static boolean loud(String name, boolean value) {
        System.out.print("[" + name + " checked] ");
        return value;
    }

    public static void main(String[] args) {
        System.out.println(loud("A", false) && loud("B", true));      // A is false: && already knows the answer
        System.out.println(loud("A", true) || loud("B", false));      // A is true:  || already knows the answer
        System.out.println(loud("A", true) && loud("B", false));      // here B is needed

        int total = 40;
        int n = 0;
        if (n != 0 && total / n > 5) {           // the guard comes first, so the division never happens
            System.out.println("high average");
        } else {
            System.out.println("no data, or a low average");
        }

        String name = null;
        if (name != null && name.length() > 0) { // the same pattern protects a method call
            System.out.println("has a name");
        } else {
            System.out.println("no name");
        }

        boolean a = true;
        boolean b = false;
        boolean c = false;
        System.out.println(a || b && c);         // && binds tighter than ||:  a || (b && c)
        System.out.println((a || b) && c);
        System.out.println(!a || b);             // ! binds tightest:  (!a) || b
    }
}
