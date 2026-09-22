public class ScopeError {
    public static void main(String[] args) {
        for (int i = 0; i < 4; i++) {
            System.out.print(i + " ");
        }
        System.out.println("finished at " + i);  // i was declared in the header, so it died with the loop
    }
}
