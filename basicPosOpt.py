import argparse
parser = argparse.ArgumentParser()

parser.add_argument("name", help="name of the user")
parser.add_argument("-a", "--age", type=int, help="age of the user")

args = parser.parse_args()

if args.age:
    print("My name is {}, I'm {} years old".format(args.name, args.age))
else:
    print("My name is {}".format(args.name))
