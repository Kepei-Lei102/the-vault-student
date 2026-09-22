public class Defaults {
    private int count;                           // no constructor written, so Java supplies an empty one
    private double total;
    private boolean done;
    private String label;

    public static void main(String[] args) {
        Defaults d = new Defaults();
        System.out.println(d.count + " " + d.total + " " + d.done + " " + d.label);
    }
}
