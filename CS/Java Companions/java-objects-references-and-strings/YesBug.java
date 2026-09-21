import java.util.Scanner;

public class YesBug {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Delete everything? ");
        String answer = keyboard.nextLine();
        System.out.println();

        System.out.println(answer);
        System.out.println(answer == "yes");           // the bug: same letters, different object
        System.out.println(answer.equals("yes"));      // the fix
    }
}
