#!/usr/bin/env python

import argparse
import os.path
import sys

from levenshtein import levenshtein_distance
from hamming import hamming_distance

def imagediff(method, file_name1, file_name2):
    
    if method == 'file size':
        try:
            size1 = os.path.getsize(file_name1)
        except os.error:
            print >> sys.stderr, "ERROR: Unable to access ", file_name1
            sys.exit(-1)
        try:
            size2 = os.path.getsize(file_name2)
        except os.error:
            print >> sys.stderr, "ERROR: Unable to access ", file_name2
        
        return float(abs(size1 - size2))/max(size1, size2)

    else:
        try:
            file1 = open(file_name1, 'r')
            string1 = file1.read()
        except IOError:
            print >> sys.stderr, "ERROR: Unable to open ", file_name1
        finally:
            file1.close()

        try:
            file2 = open(file_name2, 'r')
            string2 = file2.read()
        except IOError:
            print >> sys.stderr, "ERROR: Unable to open ", file_name2
        finally:
            file2.close()

        if method == 'levenshtein':
            try:
                return float(levenshtein_distance(string1, string2))/max(len(string1), len(string2))
            except ZeroDivisionError:
                return 1
        elif method == 'hamming':
            try:
                return float(hamming_distance(string1, string2))/min(len(string1), len(string2))
            except ZeroDivisionError:
                return 1
        else:
            print >> sys.stderr, "ERROR: Invalid method."
            sys.exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the percent difference between two images')
    
    method = parser.add_mutually_exclusive_group()
    method.add_argument('--levenshtein', action='store_true', help='Use Levenshtein edit distance')
    method.add_argument('--hamming', action='store_true', help='Use Hamming distance')
    method.add_argument('--file-size', action='store_true', help='Use file size comparison')

    parser.add_argument('file_name1', action='store')
    parser.add_argument('file_name2', action='store')

    arguments = parser.parse_args()

    if arguments.file_size:
        method = 'file size'
    elif arguments.levenshtein:
        method = 'levenshtein'
    elif arguments.hamming:
        method='hamming'
    else:
        method = ''
    
    print imagediff(method, arguments.file_name1, arguments.file_name2)
