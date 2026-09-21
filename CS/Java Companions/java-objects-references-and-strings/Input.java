import java.util.Scanner;                  // Scanner lives in the package java.util, so it must be imported

public class Input {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);     // a library class, used to make an object

        System.out.print("Name: ");
        String name = keyboard.nextLine();
        System.out.print("Age: ");
        int age = Integer.parseInt(keyboard.nextLine());

        System.out.println();
        System.out.println(name + " will be " + (age + 1) + " next year.");
    }
}
