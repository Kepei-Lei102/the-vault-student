public class Alias {
    public static void main(String[] args) {
        int p = 5;
        int q = p;                 // q gets a copy of the VALUE 5
        q++;
        System.out.println(p + " " + q);

        Counter a = new Counter();
        Counter b = a;             // b gets a copy of the REFERENCE: one object, two names
        b.click();
        b.click();
        System.out.println(a.getCount() + " " + b.getCount());
        System.out.println(a == b);

        Counter c = new Counter(2);            // a different object with the same count
        System.out.println(a == c);
        System.out.println(a.getCount() == c.getCount());

        b = new Counter(99);       // b now points somewhere else; a is untouched
        System.out.println(a + " " + b);
    }
}
