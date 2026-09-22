public class Return {
    // The first return that runs ends the method, even from inside a loop.
    public static int firstEven(int start, int stop) {
        for (int n = start; n <= stop; n++) {
            if (n % 2 == 0) {
                return n;
            }
        }
        return -1;                               // every path must return an int
    }

    public static void main(String[] args) {
        System.out.println(firstEven(3, 9) + " " + firstEven(3, 3));
    }
}
