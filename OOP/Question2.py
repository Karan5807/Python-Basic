# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date

class Person:

    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob


    def calculate_age(self):
        dob_value = date.year
        current_date = date.now().year
        age = current_date - dob_value
        return age


def main():
        name = input("Enter the Name: ")
        country = input("Enter the Country: ")
        dob = int(input("Enter the date of Birtth YYYY, MM, DD:  "))
        person1 = Person(name,country,dob)
        print(f"Name: {person1.name}")
        print(f"Country: {person1.country}")
        print(f"Age: {person1.calculate_age()}")


if __name__ == "__main__":
 main()


# d = int(date.today().year)
# print(d)
