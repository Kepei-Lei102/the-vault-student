/* Casting.java — (int), (double), truncation, widening and rounding (AP CSA 1.5.A). */
public class Casting {
    public static void main(String[] args) {
        System.out.println((int) 3.9);          // truncates: chops the decimals, does not round
        System.out.println((int) -3.9);         // truncates towards zero
        System.out.println((double) 7);

        int total = 17, n = 4;
        System.out.println((double) total / n);     // the cast binds to total FIRST: 17.0 / 4
        System.out.println((double) (total / n));   // too late: 17 / 4 is already 4
        System.out.println(total / (double) n);     // casting either one works

        double x = 2.5, y = 2.4, z = -2.6;
        System.out.println((int) (x + 0.5));    // round a non-negative double
        System.out.println((int) (y + 0.5));
        System.out.println((int) (z - 0.5));    // round a negative double
        System.out.println((int) (z + 0.5));    // the wrong idiom for a negative number

        double price = 19.99;
        int cents = (int) (price * 100);        // round-off meets truncation
        System.out.println(price * 100);
        System.out.println(cents);
        System.out.println((int) (price * 100 + 0.5));
    }
}
