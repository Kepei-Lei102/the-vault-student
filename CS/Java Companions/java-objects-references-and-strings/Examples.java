public class Examples {
    // Example 3: can a method change the caller's String?
    public static void shout(String s) {
        s = s + "!";
    }

    public static String shouted(String s) {
        return s + "!";
    }

    public static void main(String[] args) {
        // Example 1: count the objects, then trace
        Counter a = new Counter(1);
        Counter b = new Counter(1);
        Counter c = a;
        a.click();
        b = c;
        b.click();
        c = new Counter(10);
        c.click();
        System.out.println(a.getCount() + " " + b.getCount() + " " + c.getCount());
        System.out.println((a == b) + " " + (a == c));

        // Example 2: cut an address at the @
        String email = "ada.lovelace@analytical.org";
        int at = email.indexOf("@");
        String user = email.substring(0, at);
        String domain = email.substring(at + 1);
        System.out.println(at + " " + user + " " + domain);
        String initial = user.substring(0, 1);
        System.out.println(initial + " " + user.length() + " " + domain.indexOf("."));

        // Example 3
        String word = "stop";
        shout(word);
        System.out.println(word);
        word = shouted(word);
        System.out.println(word);
    }
}
