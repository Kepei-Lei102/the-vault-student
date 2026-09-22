public class Semicolon {
    public static void main(String[] args) {
        int score = 30;

        if (score >= 50);                        // the semicolon IS the body: an empty statement
        {
            System.out.println("pass");          // an ordinary block, run every time
        }
    }
}
