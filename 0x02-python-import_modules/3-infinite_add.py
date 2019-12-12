#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args = len(argv) - 1
    if args > 0:
        sum = 0
        for i in range(args):
            sum += int(argv[i + 1])
        print("{}".format(sum))
    else:
        print("0")
