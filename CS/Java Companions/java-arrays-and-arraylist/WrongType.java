import java.util.ArrayList;

public class WrongType {
    public static void main(String[] args) {
        ArrayList<int> nums = new ArrayList<int>();     // a list holds objects; write Integer
        int[] a = new int[3];
        System.out.println(a.length() + " " + nums.size);   // length is an attribute; size is a method
    }
}
