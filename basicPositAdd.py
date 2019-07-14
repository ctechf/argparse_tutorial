import argparse
parser = argparse.ArgumentParser()

parser.add_argument("x", type=int, help="First Number")
parser.add_argument("y", type=int, help="Second Number")

args = parser.parse_args()

result = args.x + args.y

print("{} + {} = {}".format(args.x, args.y, result))
