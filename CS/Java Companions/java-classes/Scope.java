public class Scope {
    private int field = 1;                       // instance scope: every method of this object can see it
    private static int shared = 2;               // class scope: shared by all objects

    public void show(int param) {                // param is local to this method
        int local = 3;                           // local: born here, dies at the closing brace
        for (int i = 0; i < 1; i++) {
            int inner = 4;                       // local to the loop body
            System.out.println(field + " " + shared + " " + param + " " + local + " " + inner);
        }
        System.out.println(field + " " + shared + " " + param + " " + local);
    }

    public static void main(String[] args) {
        new Scope().show(9);
    }
}
