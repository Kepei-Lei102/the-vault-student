/* Uninitialised.java — a variable must be given a value before it is used (AP CSA 1.4.A.1). */
public class Uninitialised {
    public static void main(String[] args) {
        int total;
        System.out.println(total);
    }
}
