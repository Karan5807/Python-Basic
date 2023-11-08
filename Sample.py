class Student:
    def __init__(self, name, section):

        if not name:
            raise ValueError("Missing Name")

        if section not in ["Lucknow", "Kolkata", "Bokaro", "Siwan"]:
            raise ValueError("Invalid House")
        self.name = name
        self.section = section


def main():
    student1 = get_student()
    print(f"{student1.name} from {student1.section}")
    


def get_student():
    name = input("Enter your Name: ")
    section = input("Enter you House: ")
    Student(name, section)
    return Student(name, section)


if __name__ == "__main__":
    main()
