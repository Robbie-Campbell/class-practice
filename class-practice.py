"""
A refresher on classes in python
"""
storage = "driverlogs.txt"

file = open(storage, "a")
read = open(storage, "r")


def read_driver_info():
    print(str(read.readlines()))


class Driver:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        include_bio = input("Do you want to enter a bio for " + str(name) + "? (y/n): ")
        if include_bio == "y":
            new_info = input("Enter your bio: ")
            self.bio = new_info
        else:
            self.bio = ""
            print("Driver info saved")

    def get_name(self):
        print("The name of the driver is ", str(self.name))

    def change_name(self):
        new = input("please enter a new name: ")
        self.name = new

    def __delete__(self):
        sure = input("Are you sure you want to delete: " + str(self.name) + " ")
        if sure == "yes":
            print(sure)
            del self.name

    def save_driver(self):
        confirm = input("Type confirm to enter driver into file: ")
        if confirm == "confirm":
            file.write(self.name + "\n")
            file.write(self.dob + " \n")
            file.write(self.bio + "\n\n")
            print("Driver info now in file.")
        else:
            print("Driver info not saved.")


Chris = Driver("Chris", "12/06/2003")

Rab = Driver("Rab", "09/10/1995")

Rab.save_driver()

Chris.save_driver()

read_driver_info()

Rab.get_name()

print(Chris.bio)

file.close()
read.close()
