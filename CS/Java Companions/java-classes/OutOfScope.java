public class OutOfScope {
    public void a() {
        int secret = 7;
    }

    public void b() {
        System.out.println(secret);              // secret lived and died inside a()
    }
}
