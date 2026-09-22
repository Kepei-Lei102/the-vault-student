/** A tiny mutable object, so that arrays and lists of objects can be shown. */
public class Tally {
    private int count;

    public Tally(int start) {
        count = start;
    }

    public void bump() {
        count++;
    }

    public int getCount() {
        return count;
    }

    public String toString() {
        return "Tally(" + count + ")";
    }
}
