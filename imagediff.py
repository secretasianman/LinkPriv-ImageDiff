#!/usr/bin/env python

import sys

from levenshtein import levenshtein_distance
from hamming import hamming_distance

def get_percent_hamming_distance(file_name1, file_name2):
    try:
        file1 = open(file_name1, 'r')
        file2 = open(file_name2, 'r')
        string1 = file1.read()
        string2 = file2.read()
        return float(hamming_distance(string1, string2))/min(len(string1), len(string2))
    except IOError:
        print >> sys.stderr, "ERROR: ", file_name1, file_name2
    finally:
        file1.close()
        file2.close()

def main():
    imgs = sys.argv[1:]

    l = len(imgs)
    tot = l*l
    count = 0
    for i1 in imgs:
        for i2 in imgs:
            count +=1
            if not count % 100:
                print >> sys.stderr, "%d/%d"%(count, tot)

            if i1 == i2:
                hm = 0
            else:
                hm = get_percent_hamming_distance(i1,i2)

            print i1,i2,hm


if __name__ == "__main__":
    main()
