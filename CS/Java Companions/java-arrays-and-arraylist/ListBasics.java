import java.util.ArrayList;

public class ListBasics {
    public static void main(String[] args) {
        ArrayList<String> queue = new ArrayList<String>();      // empty; grows as needed
        System.out.println(queue.size() + " " + queue);

        queue.add("Ada");                                       // append: returns true
        queue.add("Bob");
        queue.add("Cyd");
        queue.add(1, "Dee");                                    // insert at index 1: Bob and Cyd move right
        System.out.println(queue.size() + " " + queue);

        System.out.println(queue.get(0) + " " + queue.get(queue.size() - 1));
        String old = queue.set(2, "Bea");                       // replace: returns what was there
        String gone = queue.remove(0);                          // remove by index: returns it; everyone moves left
        System.out.println(old + " " + gone + " " + queue.size() + " " + queue);

        System.out.println(queue.get(3));                       // size is 3, so index 3 does not exist
    }
}
