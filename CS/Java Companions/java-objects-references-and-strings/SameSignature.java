public class SameSignature {
    public static int area(int side) {
        return side * side;
    }

    // Same name, same parameter types: the same signature.  A different return type does not make it a different method.
    public static double area(int side) {
        return side * side;
    }

    public static void main(String[] args) {
        System.out.println(area(4));
    }
}
