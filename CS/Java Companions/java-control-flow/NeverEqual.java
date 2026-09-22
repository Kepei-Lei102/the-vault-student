public class NeverEqual {
    public static void main(String[] args) {
        int n = 0;
        int passes = 0;
        while (n != 10 && passes < 8) {          // the  passes < 8  is only here so that this demonstration stops
            n += 3;
            passes++;
            System.out.print(n + " ");
        }
        System.out.println();
        System.out.println("n went from 9 to 12 and was never equal to 10;  n < 10  would have stopped it");
    }
}
