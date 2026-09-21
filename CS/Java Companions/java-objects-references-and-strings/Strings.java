public class Strings {
    public static void main(String[] args) {
        String s = "computer";
        //          01234567

        System.out.println(s.length());
        System.out.println(s.substring(3, 6));     // from index 3 up to BUT NOT including 6
        System.out.println(s.substring(3));        // from index 3 to the end
        System.out.println(s.substring(2, 3));     // one character, as a String
        System.out.println("[" + s.substring(8) + "]");   // legal: the empty string
        System.out.println(s.indexOf("put"));
        System.out.println(s.indexOf("t"));
        System.out.println(s.indexOf("z"));        // not found

        System.out.println("apple".compareTo("banana"));
        System.out.println("banana".compareTo("apple"));
        System.out.println("apple".compareTo("apple"));
        System.out.println("apple".compareTo("apply"));
        System.out.println("app".compareTo("apple"));
        System.out.println("Zebra".compareTo("apple"));    // capitals come before lower case

        System.out.println("a" + 1 + 2);           // left to right: "a1", then "a12"
        System.out.println(1 + 2 + "a");           // left to right: 3, then "3a"
        System.out.println("a" + (1 + 2));

        String line = "";
        line += "x";
        line += 7;
        line += 2.5;
        line += true;
        System.out.println(line);

        System.out.println(s.substring(3).indexOf("t"));   // chaining: "puter".indexOf("t")
        System.out.println(s.substring(0, 1).equals("c"));
    }
}
