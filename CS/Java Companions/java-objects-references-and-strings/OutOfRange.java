public class OutOfRange {
    public static void main(String[] args) {
        String s = "hello";
        System.out.println(s.substring(3, 5));
        System.out.println(s.substring(3, 9));     // there is no index 8
    }
}
