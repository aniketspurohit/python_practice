class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def get_older(self, years):
        self.age += years


# Worker is the inherited class
class Worker(Person):
    def __init__(self, name, age, salary):
        # In Python 3, super needn't be passed with Child class name and self keyword
        super().__init__(
            name, age
        )  # Using super, __init__ needn't be reintialised again for name, age in the Worker class
        self.salary = salary

    def __str__(self):
        return super().__str__() + " is fine"
        # text += f"{self.salary}"

    def calc_yearly_salary(self):
        return self.salary * 12


# Defining objects

w1 = Worker("aniket", 25, 230)
print(w1)
print(w1.calc_yearly_salary())
