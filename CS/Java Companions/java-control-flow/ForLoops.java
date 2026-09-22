public class ForLoops {
    public static void main(String[] args) {
        for (int i = 0; i < 4; i++) {            // 0 1 2 3: four passes, and 4 itself is never used
            System.out.print(i + " ");
        }
        System.out.println();

        for (int i = 1; i <= 4; i++) {           // 1 2 3 4
            System.out.print(i + " ");
        }
        System.out.println();

        for (int i = 10; i > 0; i -= 3) {        // any update will do
            System.out.print(i + " ");
        }
        System.out.println();

        // The same loop as a while: the three parts of the header, unpacked.
        int k = 0;                               // initialisation, once
        while (k < 4) {                          // condition, before every pass
            System.out.print(k + " ");
            k++;                                 // update, after the body
        }
        System.out.println();
        System.out.println("after the loop k is " + k);

        // Accumulate: 1 + 2 + ... + 100
        int total = 0;
        for (int i = 1; i <= 100; i++) {
            total += i;
        }
        System.out.println(total);

        // Count: how many numbers from 1 to 100 are divisible by 7?
        int sevens = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 7 == 0) {
                sevens++;
            }
        }
        System.out.println(sevens);
    }
}
