/* LogicError.java — compiles, runs, and is wrong (AP CSA 1.1.C.2).  Only testing finds this kind. */
public class LogicError {
    public static void main(String[] args) {
        int a = 70, b = 85, c = 90;
        double mean = a + b + c / 3;        // meant (a + b + c) / 3.0
        System.out.println(mean);
        System.out.println((a + b + c) / 3.0);
    }
}
