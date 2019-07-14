import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="name of the user")

args = parser.parse_args()

if args.name:
    print("Hello {}".format(args.name))
else:
    print("Hello")
