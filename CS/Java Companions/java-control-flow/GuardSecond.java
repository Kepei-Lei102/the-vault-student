public class GuardSecond {
    public static void main(String[] args) {
        int total = 40;
        int n = 0;
        if (total / n > 5 && n != 0) {           // the guard is too late
            System.out.println("high average");
        }
    }
}
