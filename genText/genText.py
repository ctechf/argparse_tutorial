import argparse
import random
parser = argparse.ArgumentParser()

parser.add_argument('name', help="name of the file")

parser.add_argument('-l', '--letters', default='0', help="letters")
parser.add_argument('-c', '--char', default='6', help="character")
parser.add_argument('-n', '--times', type=int, default='6', help="n times")

args = parser.parse_args()

name = args.name
char = int(args.char)
times = int(args.times)
lt = args.letters

if (lt == '0'):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
else:
    letters = args.letters

file = open(name, 'w')

for time in range(times):
    genarete = ''.join((random.choice(letters) for i in range(char)))
    file.write(genarete+'\n')

file.close()
