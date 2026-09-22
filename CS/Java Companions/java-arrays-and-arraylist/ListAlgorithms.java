import java.util.ArrayList;

public class ListAlgorithms {
    public static void main(String[] args) {
        ArrayList<Integer> sorted = new ArrayList<Integer>();
        for (int v : new int[] {2, 5, 9, 14}) { sorted.add(v); }

        int x = 7;                                              // insert keeping the order: find the first bigger element
        int pos = 0;
        while (pos < sorted.size() && sorted.get(pos) < x) {    // the size() check comes first: short-circuit
            pos++;
        }
        sorted.add(pos, x);
        System.out.println(sorted);

        ArrayList<String> words = new ArrayList<String>();
        for (String w : new String[] {"tea", "milk", "tea", "jam"}) { words.add(w); }
        int k = 0;                                              // delete every "tea"
        while (k < words.size()) {
            if (words.get(k).equals("tea")) { words.remove(k); } else { k++; }
        }
        System.out.println(words);

        ArrayList<Integer> p = new ArrayList<Integer>();       // two lists at once: a dot product
        ArrayList<Integer> q = new ArrayList<Integer>();
        for (int v : new int[] {1, 2, 3}) { p.add(v); q.add(v * 10); }
        int dot = 0;
        for (int i = 0; i < p.size(); i++) {
            dot += p.get(i) * q.get(i);
        }
        System.out.println(dot);

        ArrayList<Integer> r = new ArrayList<Integer>(p);      // reverse: swap ends with set
        for (int i = 0; i < r.size() / 2; i++) {
            int t = r.get(i);
            r.set(i, r.get(r.size() - 1 - i));
            r.set(r.size() - 1 - i, t);
        }
        System.out.println(r);
    }
}
