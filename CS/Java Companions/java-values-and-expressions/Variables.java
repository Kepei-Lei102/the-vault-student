/* Variables.java — declared types: int, double, boolean (AP CSA 1.2, 1.4).
   A Java variable has ONE type for its whole life, written when it is declared. */
public class Variables {
    public static void main(String[] args) {
        int score = 42;                 // a whole number
        double price = 9.5;             // a real number
        boolean passed = score >= 40;   // true or false, all lower case
        System.out.println(score);
        System.out.println(price);
        System.out.println(passed);

        score = score + 1;              // the value may change; the type may not
        System.out.println(score);

        double d = 7;                   // an int is widened to a double automatically
        System.out.println(d);          // 7.0, not 7

        int count;                      // declared, not yet initialised
        count = 3;                      // initialised here, the first time it is assigned
        System.out.println(count);
    }
}
