class Patient(object):

    def __init__(self, name, age, doctor, medication):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.medication = medication

    def __str__(self):
        return "Name: {}\nAge: {}\nMedications: {}\nDoctor: {}".format(self.name, self.age, ", ".join(self.medication), self.doctor)

class Ward(object):

    def __init__(self):
        self.d = {}

    def add(self, element):
        self.d[element.name] = element

    def remove(self, name):
        del self.d[name]

    def lookup(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

    def get_patients_by_medication(self, name):
        return [self.d[k] for k in self.d if name in self.d[k].medication]

def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House', ['penicillin', 'nexium'])
    p3 = Patient('Sam', 42, 'Gregory House', ['nexium'])

    w = Ward()
    w.add(p1)
    w.add(p2)
    w.add(p3)

    patient_list = w.get_patients_by_medication('nexium')
    assert(len(patient_list) == 2)
    assert(p1 not in patient_list)
    assert(p2 in patient_list)
    assert(p3 in patient_list)

if __name__ == '__main__':
    main()
