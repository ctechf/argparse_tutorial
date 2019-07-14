import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--country', choices=['0', '1', '2', '3'],
                    help="Select country")

args = parser.parse_args()
select = args.country

if select == '0':
    print("0 - United State")
elif select == '1':
    print("1 - Canada")
elif select == '2':
    print("2 - China")
elif select == '3':
    print("3 - Japan")
