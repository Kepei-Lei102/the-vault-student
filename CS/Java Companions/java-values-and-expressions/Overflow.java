/* Overflow.java — the range of int, overflow, and double round-off (AP CSA 1.5.B, 1.5.C). */
public class Overflow {
    public static void main(String[] args) {
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);
        System.out.println(Integer.MAX_VALUE + 1);      // wraps round, no error, no warning
        System.out.println(Integer.MIN_VALUE - 1);
        int big = 50000;
        System.out.println(big * big);                  // 2 500 000 000 does not fit
        System.out.println((double) big * big);         // a double has the room

        System.out.println(0.1 + 0.2);                  // round-off
        System.out.println(0.1 + 0.2 == 0.3);
        double sum = 0;
        for (int i = 0; i < 10; i++) {
            sum += 0.1;
        }
        System.out.println(sum);
        System.out.println(sum == 1.0);
        int cents = 0;                                  // the cure: count in whole units
        for (int i = 0; i < 10; i++) {
            cents += 10;
        }
        System.out.println(cents == 100);
    }
}
