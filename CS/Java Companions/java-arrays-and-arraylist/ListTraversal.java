import java.util.ArrayList;

public class ListTraversal {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int v : new int[] {3, 8, 8, 8, 5}) { nums.add(v); }

        for (int i = 0; i < nums.size(); i++) {                // indexed: size(), not length, and get(i), not [i]
            System.out.print(nums.get(i) + " ");
        }
        System.out.println();
        for (int n : nums) {                                    // enhanced for works on lists too
            System.out.print(n + " ");
        }
        System.out.println();

        ArrayList<Integer> a = new ArrayList<Integer>(nums);    // three copies to break in three ways
        for (int i = 0; i < a.size(); i++) {                    // FORWARD removal: after removing index 1, the next 8 slides into index 1 and is skipped
            if (a.get(i) == 8) { a.remove(i); }
        }
        System.out.println("forward:  " + a);

        ArrayList<Integer> b = new ArrayList<Integer>(nums);
        for (int i = b.size() - 1; i >= 0; i--) {               // BACKWARD removal: what slides is already behind you
            if (b.get(i) == 8) { b.remove(i); }
        }
        System.out.println("backward: " + b);

        ArrayList<Integer> c = new ArrayList<Integer>(nums);
        int i = 0;                                              // or: only advance when you did not remove
        while (i < c.size()) {
            if (c.get(i) == 8) { c.remove(i); } else { i++; }
        }
        System.out.println("careful:  " + c);

        ArrayList<Integer> d = new ArrayList<Integer>(nums);
        for (int n : d) {                                       // removing inside an enhanced for: the program stops
            if (n == 8) { d.remove(Integer.valueOf(n)); }
        }
        System.out.println("never printed");
    }
}
