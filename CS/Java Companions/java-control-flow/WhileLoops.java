import java.util.Scanner;

public class WhileLoops {
    public static void main(String[] args) {
        int fuel = 3;
        while (fuel > 0) {                       // tested BEFORE every pass, including the first
            System.out.print(fuel + " ");
            fuel--;
        }
        System.out.println("liftoff");

        int empty = 0;
        while (empty > 0) {                      // false at the start: the body runs zero times
            System.out.println("never printed");
        }

        // The digits of an integer:  % 10 reads the last digit,  / 10 removes it.
        int number = 4096;
        int digitSum = 0;
        int digits = 0;
        while (number > 0) {
            digitSum += number % 10;
            digits++;
            number /= 10;
        }
        System.out.println(digits + " digits, sum " + digitSum);

        // A sentinel loop: keep reading until the value that means "stop".
        Scanner keyboard = new Scanner(System.in);
        int count = 0;
        int sum = 0;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int passes = 0;
        int mark = Integer.parseInt(keyboard.nextLine());
        while (mark != -1) {
            count++;
            sum += mark;
            if (mark > max) { max = mark; }
            if (mark < min) { min = mark; }
            if (mark >= 50) { passes++; }
            mark = Integer.parseInt(keyboard.nextLine());
        }
        System.out.println(count + " marks, " + passes + " passes, min " + min + ", max " + max);
        System.out.println("mean " + (double) sum / count + "  (and with int division: " + sum / count + ")");
    }
}
