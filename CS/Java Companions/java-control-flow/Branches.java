public class Branches {
    // Multiway selection: the FIRST true condition wins, and at most one branch runs.
    public static String grade(int mark) {
        if (mark >= 80) {
            return "A";
        } else if (mark >= 65) {
            return "B";
        } else if (mark >= 50) {
            return "C";
        } else {
            return "U";
        }
    }

    // The same conditions in the wrong order: the first one catches almost everybody.
    public static String gradeWrongOrder(int mark) {
        if (mark >= 50) {
            return "C";
        } else if (mark >= 65) {
            return "B";
        } else if (mark >= 80) {
            return "A";
        } else {
            return "U";
        }
    }

    public static void main(String[] args) {
        int temp = 31;
        if (temp > 30) {                         // one-way: nothing happens when it is false
            System.out.println("hot");
        }
        if (temp % 2 == 0) {                     // two-way: exactly one of the two runs
            System.out.println("even");
        } else {
            System.out.println("odd");
        }

        System.out.println(grade(91) + " " + grade(65) + " " + grade(64) + " " + grade(12));
        System.out.println(gradeWrongOrder(91) + " " + gradeWrongOrder(65) + " " + gradeWrongOrder(64) + " " + gradeWrongOrder(12));

        // Separate ifs are NOT an else-if chain: every condition is tested, so several can run.
        int mark = 91;
        String awards = "";
        if (mark >= 50) { awards += "pass "; }
        if (mark >= 65) { awards += "merit "; }
        if (mark >= 80) { awards += "distinction "; }
        System.out.println(awards);
    }
}
