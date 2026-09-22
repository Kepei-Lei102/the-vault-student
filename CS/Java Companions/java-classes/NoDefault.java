public class NoDefault {
    public static void main(String[] args) {
        BankAccount a = new BankAccount();       // BankAccount wrote its own constructors, so the free one is gone
    }
}
