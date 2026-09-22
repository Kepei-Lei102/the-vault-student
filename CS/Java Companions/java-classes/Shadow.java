public class Shadow {
    private int size;

    public Shadow(int size) {
        size = size;                             // both names mean the parameter; the field is never set
    }

    public int getSize() {
        return size;
    }

    public static void main(String[] args) {
        Shadow s = new Shadow(42);
        System.out.println(s.getSize());
    }
}
