import datetime
class Person:
    def __init__(self, firstName, lastName, birth, address, phoneNumber, email):
        self.name = firstName + " " + lastName
        # self.firstName = firstName
        # self.lastName = lastName
        self.birth = birth
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
    def age(self):
        return datetime.date.today().year - self.birth.year

person = Person("Tony", "Stark", datetime.date(1970, 5, 29), "10880 Malibu Point, Malibu, California", "555 456 0987", "TSatrk@gmail.com")

print(person.name)
print(person.email)
print(person.phoneNumber)
print(person.age())