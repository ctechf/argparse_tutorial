import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="name of the user")
parser.add_argument("-a", "--age", help="age of the user")

args = parser.parse_args()

if args.name is None:
    parser.error("--name required")
else:
    print ("name =", args.name)
    print ("age =", args.age)
    

