public class NullDemo {
    public static void main(String[] args) {
        Counter spare = null;                  // a reference that points at no object
        System.out.println(spare == null);
        System.out.println("spare is " + spare);

        if (spare != null) {
            spare.click();                     // skipped: the check protects the call
        }
        System.out.println("still running");

        spare.click();                         // no object to click
        System.out.println("never printed");
    }
}
