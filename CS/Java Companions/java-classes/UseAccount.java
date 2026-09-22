public class UseAccount {
    public static void main(String[] args) {
        BankAccount ada = new BankAccount("Ada", 100.0);
        BankAccount bob = new BankAccount("Bob");
        System.out.println(ada + " | " + bob);
        System.out.println("accounts opened: " + BankAccount.getAccountsOpened());

        ada.deposit(50.0);
        System.out.println(ada.withdraw(30.0) + " " + ada.getBalance());
        System.out.println(bob.withdraw(30.0) + " " + bob.getBalance());     // fails, and costs the fee

        System.out.println(ada.transferTo(bob, 70.0) + " " + ada + " | " + bob);
        System.out.println(ada.richerOf(bob));
        System.out.println(BankAccount.OVERDRAFT_FEE);
    }
}
