public class Methods {
    // A void method: it does something and hands nothing back.
    public static void greet(String name) {
        System.out.println("  (inside greet) hello, " + name);
    }

    // A non-void method: the header promises an int, so every path must return one.
    public static int area(int side) {
        return side * side;
    }

    // Same name, different parameter list: an overload.  The signature is  area(int, int).
    public static int area(int width, int height) {
        return width * height;
    }

    // Another overload.  The signature is  area(double).
    public static double area(double radius) {
        return Math.PI * radius * radius;
    }

    // An int argument is allowed where a double is expected: widening loses nothing.
    public static double half(double x) {
        return x / 2;
    }

    // The parameter is a COPY of the argument.
    public static void addTen(int n) {
        n = n + 10;
        System.out.println("  (inside addTen) n is " + n);
    }

    public static void main(String[] args) {
        System.out.println("before the call");
        greet("Ada");                                  // control jumps into greet, then comes back here
        System.out.println("after the call");

        int a = area(4);                               // the return value is stored
        System.out.println(a + " " + area(4, 5));      // or used inside an expression
        System.out.println(area(4.0));                 // the argument's type picks the overload
        System.out.println(half(9));                   // the int 9 arrives as the double 9.0
        area(7);                                       // legal, and useless: the 49 is thrown away

        int x = 5;
        addTen(x);
        System.out.println("x is still " + x);

        System.out.println(Methods.area(3) + " " + Math.abs(-3) + " " + Integer.parseInt("42"));
    }
}
