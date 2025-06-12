# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  usually used for general utility functions

# Instance methods = Best for operations on instances of the class
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} : {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Emmanuel", "Manager")
employee2 = Employee("Oiza", "Cashier")
employee3 = Employee("Joshua", "Janitor")
employee4 = Employee("Lunix", "Cook")

print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())