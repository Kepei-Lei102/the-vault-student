public class ArrayBasics {
    public static void main(String[] args) {
        int[] marks = new int[4];                    // length fixed for ever; every slot at the default 0
        double[] prices = new double[2];
        boolean[] flags = new boolean[2];
        String[] names = new String[2];              // a reference type: every slot is null
        System.out.println(marks[0] + " " + prices[0] + " " + flags[0] + " " + names[0]);

        marks[0] = 71;                               // [] to write ...
        marks[3] = 58;
        System.out.println(marks[0] + " " + marks[3] + " length " + marks.length);   // ... and to read; .length has no brackets

        int[] primes = {2, 3, 5, 7, 11};             // an initializer list: length 5, no new needed
        System.out.println(primes.length + " " + primes[primes.length - 1]);        // the last index is length - 1

        int[] alias = primes;                        // an array is an object: this copies the reference
        alias[0] = 99;
        System.out.println(primes[0]);

        System.out.println(primes[5]);               // index 5 does not exist: the program stops here
        System.out.println("never printed");
    }
}
