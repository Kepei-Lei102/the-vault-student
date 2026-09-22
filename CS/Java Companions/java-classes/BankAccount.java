/**
 * A bank account: the class this companion writes from scratch, one section at a time.
 * The finished version is here; the sections quote the pieces as they are added.
 */
public class BankAccount {
    // ---- class variables: one copy, shared by every account ----
    private static int accountsOpened = 0;                 // how many accounts exist
    public static final double OVERDRAFT_FEE = 15.0;       // final: cannot be changed

    // ---- instance variables: every account has its own ----
    private String owner;
    private double balance;
    private int withdrawals;

    /** Opens an account with a starting balance.  Precondition: opening >= 0. */
    public BankAccount(String owner, double opening) {
        this.owner = owner;                                // this.owner is the field; owner is the parameter
        balance = opening;                                 // no clash, so no this needed
        withdrawals = 0;
        accountsOpened++;
    }

    /** Opens an empty account. */
    public BankAccount(String owner) {
        this(owner, 0.0);                                  // hand over to the other constructor
    }

    // ---- accessors: hand out a copy of the state ----
    public String getOwner() {
        return owner;
    }

    public double getBalance() {
        return balance;
    }

    public static int getAccountsOpened() {
        return accountsOpened;
    }

    // ---- mutators: change the state ----
    /** Precondition: amount > 0.  Postcondition: the balance has grown by amount. */
    public void deposit(double amount) {
        balance += amount;
    }

    /** Takes money out if it is there.  Returns whether it succeeded; charges a fee when it did not. */
    public boolean withdraw(double amount) {
        if (amount > balance) {
            balance -= OVERDRAFT_FEE;
            return false;                                  // leaves the method here; nothing below runs
        }
        balance -= amount;
        withdrawals++;
        return true;
    }

    /** Moves money into another account.  The other object is a parameter of the same class, so its private field is reachable. */
    public boolean transferTo(BankAccount other, double amount) {
        if (withdraw(amount)) {
            other.balance += amount;                       // legal: same class
            return true;
        }
        return false;
    }

    /** Which of two accounts is richer.  Passing this hands over the current object. */
    public BankAccount richerOf(BankAccount other) {
        if (other.balance > balance) {
            return other;
        }
        return this;
    }

    public String toString() {
        return owner + ": " + balance;
    }
}
