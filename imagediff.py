#!/usr/bin/env python

import sys

from levenshtein import levenshtein_distance
from hamming import hamming_distance

def main():
    if len(sys.argv) != 3:
        print "Incorrect number of arguments"
        sys.exit(1)

    else:
        try:
            file1 = open(sys.argv[1], 'r')
            file2 = open(sys.argv[2], 'r')
            print hamming_distance(file1.read(), file2.read())
            #print levenshtein_distance(file1.read(), file2.read())
        except IOError:
            print "Invalid inputs"
            sys.exit(1)

if __name__ == "__main__":
    main()
