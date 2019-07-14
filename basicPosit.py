import argparse
parser = argparse.ArgumentParser()

parser.add_argument("value", help="This is help text")
args = parser.parse_args()

print (args.value)
