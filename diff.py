#!/bin/python3

import sys
from sys import argv


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def usage():
    eprint("USAGE:")
    eprint('  %s file1 file2\n' % argv[0])


def diff(e, f):
    


if len(argv) < 3:
    eprint("PARSE ERROR: Found less than 2 arguments\n")
    usage()
    sys.exit()
if len(argv) > 3:
    eprint("PARSE ERROR: Found more than 2 arguments\n")
    usage()
    sys.exit()

with open(argv[1], 'r+t') as f1, open(argv[2], 'r+t') as f2:
    s1 = f1.read()
    s2 = f2.read()

print(diff(s1, s2))