class Patient(object):

    def __init__(self, name, age, doctor, medication):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.medication = medication

    def __str__(self):
        return "Name: {}\nAge: {}\nMedications: {}\nDoctor: {}".format(self.name, self.age, ", ".join(self.medication), self.doctor)

def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House', ['penicillin', 'nexium'])

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()
