class Employee(object):

    def __init__(self, name, id, wage=0, hours=0):
        self.name = name
        self.id = id
        self.wage = wage
        self.hours = hours

    def wages(self):
        return 0

    def __str__(self):
        return('Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.id, self.wages()))

class Manager(Employee):
    def wages(self):
        return self.wage / 52

class AssemblyWorker(Employee):
    def wages(self):
        return self.wage * self.hours
