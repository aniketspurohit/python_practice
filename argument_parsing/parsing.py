import sys
import getopt  # core library for optional argument parsing

# for i in range(5):
#     print(sys.argv[i])  # Prints parsing.py q w e r (i/p: python parsing.py q w e r)

# print(sys.argv)

filename = "text.txt"
msg = "Aniket"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    if opt == "-m":
        message = arg

with open(filename, "w+") as f:
    f.write(message)

# Note: Use "" to pass a sentence in one value
