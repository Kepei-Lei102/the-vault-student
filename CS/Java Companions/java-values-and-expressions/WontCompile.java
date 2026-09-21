/* WontCompile.java — two type mistakes the COMPILER catches, before anything runs (AP CSA 1.1.B, 1.4.A).
   javac refuses to produce a program until both are fixed.  Each would run "fine" in Python. */
public class WontCompile {
    public static void main(String[] args) {
        int half = 7 / 2.0;             // 1: a double will not go into an int without a cast

        int score = 40;
        score = "forty";                // 2: a variable keeps the type it was declared with
    }
}
