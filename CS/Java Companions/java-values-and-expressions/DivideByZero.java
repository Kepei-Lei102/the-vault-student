/* DivideByZero.java — compiles without complaint, fails while running (AP CSA 1.1.C, 1.3.C.6). */
public class DivideByZero {
    public static void main(String[] args) {
        int sweets = 12;
        int children = 0;
        System.out.println("sharing...");
        System.out.println(sweets / children);      // ArithmeticException: the program stops here
        System.out.println("this line never runs");
    }
}
