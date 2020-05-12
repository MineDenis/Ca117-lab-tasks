class BankAccount(object):
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, first, last, balance=0, employee_number=next_account_number):
        self.name = first, last
        self.employee_number = BankAccount.next_account_number
        self.balance = balance
        BankAccount.next_account_number += 1

    def lodge(self, other):
        self.balance += other
        BankAccount.total_lodgements += 1

    def __add__(self, other):
        self.balance += other
        BankAccount.total_lodgements += 1
        return self

    def apply_interest(self):
        self.balance = self.balance * BankAccount.interest_rate + self.balance
        return self

    def __str__(self):
        return 'Name: {}\nAccount number: {}\nBalance: {:.2f}'.format((" ".join(self.name)), self.employee_number, self.balance)
