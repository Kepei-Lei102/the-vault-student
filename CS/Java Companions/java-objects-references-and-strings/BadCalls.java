public class BadCalls {
    public static void greet(String name) {
        System.out.println("hello, " + name);
    }

    public static int area(int width, int height) {
        return width * height;
    }

    public static void main(String[] args) {
        int r = greet("Ada");          // a void method has no value to store
        int a = area(4);               // no method called area takes one int
        int b = area(4, "5");          // right number of arguments, wrong type
        int c = area(2.5, 4);          // a double will not narrow to an int by itself
    }
}
