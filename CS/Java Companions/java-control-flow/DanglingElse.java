public class DanglingElse {
    public static void main(String[] args) {
        boolean member = true;
        int age = 15;

        // The layout says the else belongs to  if (member).  The compiler pairs it with the NEAREST if.
        if (member)
            if (age >= 18)
                System.out.println("adult member");
        else
            System.out.println("not a member");

        // Braces say what is meant.
        if (member) {
            if (age >= 18) {
                System.out.println("adult member");
            }
        } else {
            System.out.println("not a member");
        }
        System.out.println("done");
    }
}
