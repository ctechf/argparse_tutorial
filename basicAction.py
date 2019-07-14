import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", required=True, action="append", help="name of the user")

args = parser.parse_args()

for name in args.name:
    print("My name is {}".format(name))
