/**
 * A hand tally counter: the clicker a steward uses to count people through a gate.
 * This class is here to be USED, not written.  Read it the way you would read a library's documentation.
 */
public class Counter {
    private int count;                     // the attribute: every Counter object has its own

    /** Makes a counter that starts at 0. */
    public Counter() {
        count = 0;
    }

    /** Makes a counter that starts at start.  Precondition: start >= 0. */
    public Counter(int start) {
        count = start;
    }

    /** Adds 1.  Postcondition: the count is one more than it was. */
    public void click() {
        count++;
    }

    /** Adds n.  Precondition: n >= 0. */
    public void add(int n) {
        count += n;
    }

    /** Returns the current count, and changes nothing. */
    public int getCount() {
        return count;
    }

    /** Returns a description such as "Counter[3]". */
    public String toString() {
        return "Counter[" + count + "]";
    }
}
