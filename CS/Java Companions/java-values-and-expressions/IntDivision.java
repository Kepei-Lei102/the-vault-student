/* IntDivision.java — int and double arithmetic, % and precedence (AP CSA 1.3.C).
   Rule: int with int gives int.  If either side is a double, the result is a double. */
public class IntDivision {
    public static void main(String[] args) {
        System.out.println(7 / 2);          // int / int: the whole-number part only
        System.out.println(7 / 2.0);        // one double is enough
        System.out.println(7.0 / 2);
        System.out.println(7 % 2);          // remainder
        System.out.println(2 / 7);          // 0, because 2 / 7 is less than one whole
        System.out.println(2 % 7);          // 2: seven goes into two zero times, 2 left over
        System.out.println(3 + 4 * 2);      // * / % before + -
        System.out.println((3 + 4) * 2);
        System.out.println(1 / 2 * 6.0);    // left to right: 1 / 2 is 0 first, then 0 * 6.0
        System.out.println(6.0 * 1 / 2);    // left to right: 6.0 * 1 is 6.0, then 6.0 / 2
        int total = 17, n = 4;
        System.out.println(total / n);      // the classic average bug
        System.out.println(total % n);
        int minutes = 135;
        System.out.println(minutes / 60 + " h " + minutes % 60 + " min");
    }
}
