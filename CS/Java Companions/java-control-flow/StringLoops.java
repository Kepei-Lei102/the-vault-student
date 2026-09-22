public class StringLoops {
    public static void main(String[] args) {
        String word = "banana";

        // Visit every character: indices 0 to length() - 1.
        int vowels = 0;
        for (int i = 0; i < word.length(); i++) {
            String ch = word.substring(i, i + 1);
            if (ch.equals("a") || ch.equals("e") || ch.equals("i") || ch.equals("o") || ch.equals("u")) {
                vowels++;
            }
        }
        System.out.println(vowels + " vowels");

        // Build a new string with the characters reversed.
        String reversed = "";
        for (int i = word.length() - 1; i >= 0; i--) {
            reversed += word.substring(i, i + 1);
        }
        System.out.println(reversed);

        // Count the two-letter substrings equal to "an".  The last legal start is length() - 2.
        int count = 0;
        for (int i = 0; i <= word.length() - 2; i++) {
            if (word.substring(i, i + 2).equals("an")) {
                count++;
            }
        }
        System.out.println(count + " times \"an\"");

        // Does ANY character have a property?  Start by assuming no, and let one find change it.
        String code = "room4b";
        boolean hasDigit = false;
        for (int i = 0; i < code.length(); i++) {
            String ch = code.substring(i, i + 1);
            if (ch.compareTo("0") >= 0 && ch.compareTo("9") <= 0) {
                hasDigit = true;
            }
        }
        System.out.println(hasDigit);
    }
}
