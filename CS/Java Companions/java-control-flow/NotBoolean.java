public class NotBoolean {
    public static void main(String[] args) {
        int n = 5;
        String s = "hello";

        if (n) {                                 // Python allows this.  Java wants a boolean.
            System.out.println("non-zero");
        }
        if (n = 5) {                             // one = is assignment, and its value is an int
            System.out.println("five");
        }
        if (1 < n < 10) {                        // 1 < n is a boolean, and a boolean cannot be < 10
            System.out.println("in range");
        }
        if (s.length()) {                        // Python's  if s:  has no Java form
            System.out.println("not empty");
        }
    }
}
