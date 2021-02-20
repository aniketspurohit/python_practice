class Person:
    count = 0  # global variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1  # global variable

    def __del__(self):
        Person.count -= 1
        print(f"Object {self.name} has been deleted. Number of persons:{Person.count}")

    def __str__(self):
        return (
            f"{self.name}, {self.age}"  # __str__ should return the values and not print
        )


a1 = Person("an", 24)

print(f"Number of persons:{Person.count}")
print(a1)

del a1
