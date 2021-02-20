""" Decorators:
"""


def my_decorator(function):
    def wrapper(*args, **kwargs):
        """Using args and kwargs help in generalising the wrapper function.
        Any type of parameter can be passed."""
        function(*args, **kwargs)
        print("I am about to decorate your function!!")

    return wrapper


@my_decorator
def hello_world(name):
    print(f"Hello hello {name}")


hello_world("aniket")
