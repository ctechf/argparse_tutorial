import argparse
parser = argparse.ArgumentParser()

parser.add_argument("fname", help="First Name")
parser.add_argument("lname", help="Second Name")

args = parser.parse_args()

print("Hello {} {}!".format(args.fname, args.lname))
