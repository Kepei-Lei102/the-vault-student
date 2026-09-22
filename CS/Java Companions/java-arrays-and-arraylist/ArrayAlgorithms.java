public class ArrayAlgorithms {
    public static void main(String[] args) {
        int[] a = {4, 9, 2, 9, 7};

        int max = a[0];                              // maximum: start with the first element, not with 0
        int sum = 0;
        for (int x : a) {
            if (x > max) { max = x; }
            sum += x;
        }
        System.out.println("max " + max + ", sum " + sum + ", mean " + (double) sum / a.length);

        boolean anyOdd = false;                      // "at least one": start false, a find sets true
        boolean allPositive = true;                  // "all": start true, a failure sets false
        int count = 0;
        for (int x : a) {
            if (x % 2 == 1) { anyOdd = true; }
            if (x <= 0) { allPositive = false; }
            if (x > 5) { count++; }
        }
        System.out.println(anyOdd + " " + allPositive + " " + count + " above 5");

        int rises = 0;                               // consecutive pairs: i and i + 1, so i stops at length - 2
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i + 1] > a[i]) { rises++; }
        }
        System.out.println(rises + " rises");

        boolean dup = false;                         // duplicates: every pair, each once
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] == a[j]) { dup = true; }
            }
        }
        System.out.println("duplicate? " + dup);

        int[] shifted = new int[a.length];           // shift left by one into a NEW array; the last slot stays 0
        for (int i = 0; i < a.length - 1; i++) {
            shifted[i] = a[i + 1];
        }
        int[] rotated = new int[a.length];           // rotate left by one: the first element wraps to the end
        for (int i = 0; i < a.length; i++) {
            rotated[i] = a[(i + 1) % a.length];
        }
        System.out.println(java.util.Arrays.toString(shifted) + " " + java.util.Arrays.toString(rotated));

        for (int i = 0; i < a.length / 2; i++) {     // reverse in place: swap ends, walk to the middle
            int t = a[i];
            a[i] = a[a.length - 1 - i];
            a[a.length - 1 - i] = t;
        }
        System.out.println(java.util.Arrays.toString(a));
    }
}
