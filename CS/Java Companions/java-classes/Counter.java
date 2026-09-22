public class Counter {
    private static int created = 0;
    private int id;

    public Counter() {
        created++;
        id = created;
    }

    public int getId() {
        return id;
    }

    public static int getCreated() {
        return created;
    }

    public static void main(String[] args) {
        Counter a = new Counter();
        Counter b = new Counter();
        Counter c = new Counter();
        System.out.println(a.getId() + " " + b.getId() + " " + c.getId() + " | " + Counter.getCreated());
    }
}
