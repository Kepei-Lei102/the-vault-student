public class AssignTrap {
    public static void main(String[] args) {
        boolean finished = false;

        if (finished = true) {                   // compiles: the value of the assignment IS a boolean
            System.out.println("the game is over");
        }
        System.out.println(finished);

        boolean paused = false;
        if (paused) {                            // the safe habit: never compare a boolean with true
            System.out.println("paused");
        }
        if (!paused) {
            System.out.println("running");
        }
    }
}
