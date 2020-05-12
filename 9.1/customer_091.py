class Customer(object):

    discountprice = 0

    def __init__(self, name, balance, road, estate, county):
        self.name = name
        self.balance = balance
        self.road = road
        self.estate = estate
        self.county = county

    def owes(self):
        if self.discountprice != 0:
            return self.balance - (self.balance / self.discountprice)
        return self.balance

    def __str__(self):
        return('{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: {}%\nAmount due: {:.2f}'.format(self.name, self.road, self.estate, self.county, self.balance, self.discountprice, self.owes()))

class ValuedCustomer(Customer):
    discountprice = 10
