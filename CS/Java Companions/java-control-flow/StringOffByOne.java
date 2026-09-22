public class StringOffByOne {
    public static void main(String[] args) {
        String word = "cat";
        for (int i = 0; i <= word.length(); i++) {            // <= goes one step too far
            System.out.println(word.substring(i, i + 1));
        }
    }
}
