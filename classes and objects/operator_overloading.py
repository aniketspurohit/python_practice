# What happens if 2 objects are added/subtracted? This is the concept of Operator Overloading

# The code is self explanatory

# There are several methods used in class Vector. These are dunder methods. These methods are called implicitly.
# These methods help in implementing different operations with the objects.

import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Without this, two vector objects cannot be added"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Without this, two vector objects cannot be subtracted. Same can be said about mul and div."""
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        """ Same as __str__. The only difference is that __repr__ is the formal representation of an object. 
        __str__ is informal."""
        return f"({self.x}, {self.y})"

    def __call__(self):
        print("Hello, I am being called!")

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        """Used to return size/lengths of objects(int onlY)"""
        pass


v1 = Vector(2, 3)
v2 = Vector(3, 4)

print(f"v1:{v1}", f"v2:{v2}")

v_add = v1 + v2
v_sub = v1 - v2

print(f"v_add:{v_add}", f"v_sub:{v_sub}")

v_add()  # The __call__ function is called

print(eval(repr(v1 + v2)))

print(abs(v1))
