public class Private {
    public static void main(String[] args) {
        BankAccount ada = new BankAccount("Ada", 100.0);
        ada.balance = 1000000.0;                 // private: only BankAccount's own code may touch it
        System.out.println(ada.balance);
    }
}
