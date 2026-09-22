import java.util.ArrayList;

public class SearchSort {
    public static int linear(int[] a, int target) {            // from the left; returns -1 when absent
        for (int i = 0; i < a.length; i++) {
            if (a[i] == target) { return i; }
        }
        return -1;
    }

    public static int binary(int[] a, int target, int lo, int hi) {   // a must be sorted; recursive
        if (lo > hi) { return -1; }
        int mid = (lo + hi) / 2;
        System.out.print("[" + lo + "," + hi + "] ");
        if (a[mid] == target) { return mid; }
        if (a[mid] < target) { return binary(a, target, mid + 1, hi); }
        return binary(a, target, lo, mid - 1);
    }

    public static void selectionSort(int[] a) {                // pass k: find the smallest of the unsorted part and swap it into place k
        for (int k = 0; k < a.length - 1; k++) {
            int small = k;
            for (int j = k + 1; j < a.length; j++) {
                if (a[j] < a[small]) { small = j; }
            }
            int t = a[k]; a[k] = a[small]; a[small] = t;
            System.out.print(java.util.Arrays.toString(a) + " ");
        }
        System.out.println();
    }

    public static void insertionSort(int[] a) {                // pass k: slide a[k] left through the sorted part until it fits
        for (int k = 1; k < a.length; k++) {
            int v = a[k];
            int j = k - 1;
            while (j >= 0 && a[j] > v) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = v;
            System.out.print(java.util.Arrays.toString(a) + " ");
        }
        System.out.println();
    }

    public static void mergeSort(int[] a, int lo, int hi) {    // split until one element, merge sorted halves
        if (lo >= hi) { return; }
        int mid = (lo + hi) / 2;
        mergeSort(a, lo, mid);
        mergeSort(a, mid + 1, hi);
        int[] tmp = new int[hi - lo + 1];                       // merge the two sorted halves into tmp
        int i = lo;
        int j = mid + 1;
        int k = 0;
        while (i <= mid && j <= hi) {
            if (a[i] <= a[j]) {
                tmp[k] = a[i];
                i++;
            } else {
                tmp[k] = a[j];
                j++;
            }
            k++;
        }
        while (i <= mid) { tmp[k] = a[i]; i++; k++; }
        while (j <= hi) { tmp[k] = a[j]; j++; k++; }
        for (int t = 0; t < tmp.length; t++) { a[lo + t] = tmp[t]; }
        System.out.print("merged " + lo + ".." + hi + ": " + java.util.Arrays.toString(a) + " ");
    }

    public static int[] copyOf(int[] a) {                       // a fresh array with the same values
        int[] b = new int[a.length];
        for (int i = 0; i < a.length; i++) { b[i] = a[i]; }
        return b;
    }

    public static void main(String[] args) {
        int[] a = {29, 3, 17, 8, 12};
        System.out.println(linear(a, 17) + " " + linear(a, 5));
        int[] s = {3, 8, 12, 17, 29, 41, 50};
        System.out.println("-> " + binary(s, 41, 0, s.length - 1));
        System.out.println("-> " + binary(s, 10, 0, s.length - 1));
        selectionSort(copyOf(a));
        insertionSort(copyOf(a));
        mergeSort(a, 0, a.length - 1);
        System.out.println();
    }
}
