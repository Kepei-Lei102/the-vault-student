public class Immutable {
    public static void main(String[] args) {
        String word = "lantern";
        word.substring(0, 4);              // builds "lant" and throws it away
        System.out.println(word);

        word = word.substring(0, 4);       // keeps it: word now points at the NEW string
        System.out.println(word);

        String first = "rain";
        String second = first;             // two names, one String object
        first += "bow";                    // builds "rainbow" and re-points first
        System.out.println(first + " " + second);
    }
}
