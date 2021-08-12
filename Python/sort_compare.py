import sys
import elementary_sorts


def main(args):
    alg1 = args[1]
    alg2 = args[2]
    print(alg1, alg2)


if __name__ == 'main':
    print('Hello')
    sys.stdout.write(str(sys.argv))
    main(sys.argv)
