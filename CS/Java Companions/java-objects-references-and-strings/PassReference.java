public class PassReference {
    // c is a copy of the caller's reference, so it points at the caller's object.
    public static void clickTwice(Counter c) {
        c.click();
        c.click();
    }

    // Re-pointing the copy does nothing to the caller's variable.
    public static void replace(Counter c) {
        c = new Counter(1000);
        System.out.println("  (inside replace) c is " + c);
    }

    public static void main(String[] args) {
        Counter gate = new Counter(5);

        clickTwice(gate);
        System.out.println(gate);

        replace(gate);
        System.out.println(gate);
    }
}
