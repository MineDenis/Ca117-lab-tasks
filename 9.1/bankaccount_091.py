class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043
    account_type = 'General'

    def __init__(self, first, last, balance=0, id_number=next_account_number):
        self.name = first, last
        self.id_number = BankAccount.next_account_number
        self.balance = balance
        BankAccount.next_account_number += 1

    def lodge(self, other):
        self.balance += other

    def __add__(self, other):
        self.balance += other
        return self

    def withdraw(self, other):
        if other > self.balance:
            print('Insufficient funds available')
        else:
            self.balance -= other

    def __str__(self):
        return 'Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}'.format((" ".join(self.name)), self.id_number, self.account_type, self.balance)

class CurrentAccount(BankAccount):
    account_type = 'Current'
    overdraft = -1000

    def withdraw(self, other):
        if self.balance < 0:
            print('Insufficient funds available')
        else:
            self.balance -= other

    def __str__(self):
        return 'Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nOverdraft: {:.2f}'.format((" ".join(self.name)), self.id_number, self.account_type, self.balance, self.overdraft)
class SavingsAccount(BankAccount):
    account_type = 'Savings'
    interest = 0.01

    def withdraw(self, other):
        if self.balance < other:
            print('Insufficient funds available')
        else:
            self.balance -= other

    def apply_interest(self):
        self.balance = self.balance * self.interest + self.balance
        return self

    def __str__(self):
        return 'Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nInterest rate: {:.2f}'.format((" ".join(self.name)), self.id_number, self.account_type, self.balance, self.interest)
