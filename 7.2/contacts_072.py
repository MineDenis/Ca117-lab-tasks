class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):
    def __init__(self, d=None):
        if d is None:
            d = {}
        self.d = d

    def add_contact(self, con):
        self.d[con.name] = con

    def del_contact(self, con):
        if con in self.d:
            del self.d[con]

    def get_contact(self, con):
        if con in self.d:
            return "{} {} {}".format(self.d[con].name, self.d[con].phone, self.d[con].email)
        else:
            return "None"

    def __str__(self):
        lis = []
        lis.append("Contact list")
        lis.append("-" * len("Contact list"))
        for i in sorted(self.d.keys()):
            lis.append("{} {} {}".format(self.d[i].name, self.d[i].phone, self.d[i].email))
        return "\n".join(lis)

import sys

def main():
    cl = ContactList()
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)

    c = cl.get_contact('Jimmy')
    print(c)
    c = cl.get_contact('Mary')
    print(c)

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()
