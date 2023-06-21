import argparse


parser = argparse.ArgumentParser(description='Calculate a student\'s average grade')
parser.add_argument('grades', metavar='G', type=float, nargs='+',
                    help='list of grades')
parser.add_argument('-f', '--float', type=int, default=2,
                    help='number of decimal places (default: 2)')

args = parser.parse_args()

avg_grade = sum(args.grades) / len(args.grades)

out = f'Average grade: {avg_grade:.{args.float}f}'

print(out)

# python3 Q2.2.py 20 23.2 98.22 --float 3