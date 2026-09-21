/* CompoundAssign.java — += -= *= /= %= and x++ / x-- (AP CSA 1.6). */
public class CompoundAssign {
    public static void main(String[] args) {
        int x = 7;
        x += 3;     System.out.println(x);      // x = x + 3
        x -= 4;     System.out.println(x);
        x *= 5;     System.out.println(x);
        x /= 4;     System.out.println(x);      // int division: 30 / 4
        x %= 4;     System.out.println(x);      // 7 % 4
        x++;        System.out.println(x);      // add one
        x--;        System.out.println(x);      // subtract one
        double d = 7;
        d /= 2;     System.out.println(d);      // the variable is a double, so 3.5
    }
}
