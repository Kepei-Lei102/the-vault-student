/* MathDemo.java — the Math class methods on the AP Java Quick Reference (AP CSA 1.11). */
public class MathDemo {
    public static void main(String[] args) {
        System.out.println(Math.abs(-7));           // int in, int out
        System.out.println(Math.abs(-7.5));         // double in, double out
        System.out.println(Math.pow(2, 10));        // ALWAYS a double: 1024.0
        int p = (int) Math.pow(2, 10);              // cast it if you need an int
        System.out.println(p);
        System.out.println(Math.sqrt(2));
        System.out.println(Math.sqrt(16));          // 4.0, still a double

        // Math.random() is a double r with 0.0 <= r < 1.0.  A die: 1, 2, 3, 4, 5 or 6.
        int lowest = 99, highest = -99;
        for (int i = 0; i < 100000; i++) {
            int die = (int) (Math.random() * 6) + 1;
            if (die < lowest)  lowest = die;
            if (die > highest) highest = die;
        }
        System.out.println("die: " + lowest + " to " + highest);

        lowest = 99; highest = -99;                 // the classic bug: cast too early
        for (int i = 0; i < 100000; i++) {
            int die = (int) Math.random() * 6 + 1;  // (int) binds to Math.random() alone: always 0
            if (die < lowest)  lowest = die;
            if (die > highest) highest = die;
        }
        System.out.println("bug: " + lowest + " to " + highest);
    }
}
