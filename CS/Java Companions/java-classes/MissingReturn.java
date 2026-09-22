public class MissingReturn {
    public static int broken(int n) {
        if (n > 0) {
            return n;
        }
    }                                            // a path with no return: the compiler refuses
}
