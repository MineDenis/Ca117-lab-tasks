class user:
    pass

user1 = user()
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name, user1.last_name)

first_name = "Arthur"
last_name = "Clarke"
# Even if we use the same name variables we do not overwrite the first and last names assigned to the users

user2 = user()

user2.first_name = "Frank"
user2.last_name = "Michale"

print(user2.first_name, user2.last_name)
print(user1.first_name, user1.last_name)
print(first_name, last_name)
#keeps all the data seperate even though basically the same name
#if user1.age = 32 and you havent assigned an 3age for user2.age then you can not use the variable age for user 2

import datetime

class user:
    """ A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user information."""
    
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        user = user("Dave pussy muncher", "20010327")
        print(user.name)
        print(user.birthday)
    # I am here

    #to extract pieces from a init variable we can do split
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[:4])
        mm = int(self.birthday[4: 6])
        dd = int(self.birthday[6: 8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
user = user("Dave Bowman", "19710315")
print(user.age())
