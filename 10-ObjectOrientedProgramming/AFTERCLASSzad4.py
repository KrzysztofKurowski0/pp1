from Classes import Bank

Account = Bank("12 3456 5555 9090 1111 0000 7722")
Account.status()
Account.deposit(25.30)
Account.status()
Account.withdraw(31.70)
Account.status()
Account.withdraw(14)
Account.status()