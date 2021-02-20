def logged(function):
    def wrapper(*args, **kwargs):
        val = function(*args, **kwargs)
        with open("logfile.txt", "a+") as f:
            fname = function.__name__
            f.write(f"{fname} returned {val}\n")
        return val

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(2, 3))
