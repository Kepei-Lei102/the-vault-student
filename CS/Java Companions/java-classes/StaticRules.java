public class StaticRules {
    private int mine = 5;
    private static int ours = 7;

    public static int classMethod() {
        return ours + 1;                         // fine: a class variable
    }

    public static int alsoClassMethod() {
        return mine;                             // no object here: which object's mine?
    }

    public static int usingThis() {
        return this.mine;                        // class methods have no this
    }
}
