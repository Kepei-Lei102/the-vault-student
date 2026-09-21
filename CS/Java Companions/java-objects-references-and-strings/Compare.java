public class Compare {
    public static void main(String[] args) {
        int age = 17;
        boolean adult = age >= 18;                 // a comparison IS a value, of type boolean
        System.out.println(adult);
        System.out.println(age != 18);
        System.out.println(7 / 2 == 3);
        System.out.println(0.1 + 0.2 == 0.3);      // round-off: compare doubles with a tolerance
        System.out.println(Math.abs((0.1 + 0.2) - 0.3) < 1e-9);

        Counter x = new Counter(3);
        Counter y = new Counter(3);
        System.out.println(x == y);                // two objects
        System.out.println(x != null);
    }
}
