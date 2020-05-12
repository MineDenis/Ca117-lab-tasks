class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount
        return self.balance

    def withdraw(self, ammount):
        if self.balance - ammount < 0:
            print("Insufficient funds available")
        else:
            self.balance -= ammount
        return self.balance

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)

def main():
    b1 = BankAccount()
    print(b1)
    b1.withdraw(1)
    b1.deposit(100)
    b1.deposit(150)
    print(b1)
    b1.withdraw(50)
    print(b1)
    b1.deposit(20)
    b1.withdraw(100)
    print(b1)

    b2 = BankAccount(1000)
    b2.deposit(1)
    b2.withdraw(2000)
    print(b2)
    b2.withdraw(1001)
    print(b2)

if __name__ == '__main__':
    main()
