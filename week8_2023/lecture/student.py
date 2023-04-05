import sys

class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"the student {self.name}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return ":D"
            case _:
                return ":("
    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Haus","Test"]:
                raise ValueError("Invalid")
        self._house = house



def main():
    student = get_student()
    if student.name == "Padma":
            student.house = "Ravenclaw"
    print(student.charm())
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name, house, patronus)
    except ValueError:
        sys.exit("Stop")

if __name__ == '__main__':
    main()