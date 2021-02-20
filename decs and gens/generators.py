"""
This is the example for custom infinite generator.

Note: If the condition exhausts, StopIteration is raised.
"""


def gen():
    res = 1
    while True:
        yield res
        res += 1


val = gen()

for i in range(10):
    print(next(val))
