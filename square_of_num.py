import sys

if len(sys.argv) != 2:
    print("Usage: python square_of_num.py <number>")
    sys.exit(1)

num = int(sys.argv[1])
print("Square of", num, "is", num * num)
