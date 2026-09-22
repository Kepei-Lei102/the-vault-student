public class Nested {
    public static void main(String[] args) {
        for (int row = 1; row <= 3; row++) {                   // for EACH row ...
            for (int col = 1; col <= 4; col++) {               // ... the inner loop runs from start to finish
                System.out.print(row * col + "\t");
            }
            System.out.println();
        }

        for (int row = 1; row <= 4; row++) {                   // the inner limit depends on the outer variable
            for (int star = 1; star <= row; star++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Statement execution counts: how many times does the innermost line run?
        int n = 10;
        int square = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                square++;
            }
        }
        int triangle = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                triangle++;
            }
        }
        int halving = 0;
        for (int i = 1000; i > 0; i /= 2) {
            halving++;
        }
        System.out.println(square + " " + triangle + " " + halving);
    }
}
