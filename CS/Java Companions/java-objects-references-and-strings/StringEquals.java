public class StringEquals {
    public static void main(String[] args) {
        String a = "hi";
        String b = "hi";
        String c = new String("hi");
        String d = "h";
        d += "i";                          // built while the program runs

        System.out.println(a + " " + b + " " + c + " " + d);
        System.out.println(a == b);        // true, by an accident of how literals are stored
        System.out.println(a == c);
        System.out.println(a == d);
        System.out.println(a.equals(b) + " " + a.equals(c) + " " + a.equals(d));
        System.out.println("Hi".equals(a));
    }
}
