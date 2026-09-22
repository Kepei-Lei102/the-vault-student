import java.util.ArrayList;

public class Wrappers {
    public static void main(String[] args) {
        ArrayList<Integer> scores = new ArrayList<Integer>();   // a list holds objects, so int becomes Integer
        scores.add(90);                                         // autoboxing: the int 90 becomes an Integer object
        scores.add(75);
        int first = scores.get(0);                              // unboxing: the Integer becomes an int
        int total = scores.get(0) + scores.get(1);              // unboxed for the +
        System.out.println(first + " " + total);

        Double d = 2.5;                                         // boxing on assignment
        double e = d * 2;                                       // unboxing for the *
        System.out.println(e + " " + Integer.parseInt("42") + " " + Double.parseDouble("3.5"));

        Integer a = 1000;
        Integer b = 1000;
        System.out.println((a == b) + " " + a.equals(b));      // two objects: == compares references
        Integer p = 100;
        Integer q = 100;
        System.out.println((p == q) + " " + p.equals(q));      // small values are shared, which makes == LOOK safe
    }
}
