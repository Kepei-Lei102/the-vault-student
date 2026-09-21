public class Create {
    public static void main(String[] args) {
        Counter gate = new Counter();          // the constructor with the signature Counter()
        Counter stand = new Counter(250);      // the constructor with the signature Counter(int)

        gate.click();
        gate.click();
        stand.add(30);

        System.out.println(gate.getCount());   // each object has its own count
        System.out.println(stand.getCount());
        System.out.println("gate is " + gate); // + calls gate.toString() for you
        System.out.println(stand);             // so does println

        Object plain = new Object();           // a class with no toString of its own
        System.out.println(plain.toString().substring(0, 17));
    }
}
