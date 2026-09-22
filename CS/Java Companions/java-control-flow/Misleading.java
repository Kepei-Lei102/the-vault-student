public class Misleading {
    public static void main(String[] args) {
        int score = 30;

        if (score >= 50)
            System.out.println("pass");
            System.out.println("certificate printed");     // indented like the line above; NOT inside the if

        if (score >= 50) {
            System.out.println("pass");
            System.out.println("certificate printed");     // the braces put it inside
        }
        System.out.println("done");
    }
}
