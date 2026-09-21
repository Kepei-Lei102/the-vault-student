/* Output.java — print, println and the three escape sequences (AP CSA 1.3.A, 1.3.B).
   Compile:  javac Output.java        Run:  java Output                          */
public class Output {
    public static void main(String[] args) {
        System.out.print("one ");
        System.out.print("two ");          // print stays on the same line
        System.out.println("three");       // println moves to a new line AFTER printing
        System.out.println();              // an empty println is a blank line
        System.out.println("She said \"hi\".");      //  \"  a double quote inside a string
        System.out.println("C:\\Users\\david");      //  \\  one backslash
        System.out.println("line 1\nline 2");        //  \n  a new line inside one string
        System.out.println("total: " + 3 + 4);       // + with a String joins, left to right
        System.out.println("total: " + (3 + 4));     // brackets make the sum happen first
        System.out.println(3 + 4 + " is the total"); // here 3 + 4 is met first, so it adds
    }
}
