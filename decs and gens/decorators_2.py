import time


def timed(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        fname = function.__name__
        print(f"{fname} took {end-start} seconds!")
        return {}

    return wrapper


@timed
def printing(x):
    for i in range(1000):
        print(23)


printing("aniket")
