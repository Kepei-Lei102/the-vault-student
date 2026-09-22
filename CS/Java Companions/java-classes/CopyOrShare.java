import java.util.ArrayList;

public class CopyOrShare {
    private ArrayList<String> log;

    public CopyOrShare(ArrayList<String> log) {
        this.log = new ArrayList<String>(log);   // a COPY: later changes to the caller's list do not reach us
    }

    public int size() {
        return log.size();
    }

    public static void main(String[] args) {
        ArrayList<String> events = new ArrayList<String>();
        events.add("start");
        CopyOrShare keeper = new CopyOrShare(events);
        events.add("later");                     // the caller changes its own list afterwards
        System.out.println(events.size() + " " + keeper.size());
    }
}
