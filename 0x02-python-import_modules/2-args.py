#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("{:d} arguments.".format(args - 1))
    else:
        if args == 2:
            print("{:d} argument:".format(args - 1))
        else:
            print("{:d} arguments:".format(args - 1))
        for arg in range(1, args):
            print("{:d}: {}".format(arg, (sys.argv[arg])))
