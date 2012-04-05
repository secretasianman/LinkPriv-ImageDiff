#!/usr/bin/env python

from itertools import combinations
import os.path as path

from imagediff import imagediff
from webkit2png import generate_image

def main(url):

    generate_image(url, 'dummy')

#    url_partition = url.partition('?')
#    args = url_partition[2].split('&')

#    arg_combinations = [arg_combination for i in range (len(args) + 1)
#                        for arg_combination in combinations(args, i)]

#    print arg_combinations
    
    # Image Gen
#    for i, arg_combination in enumerate(reversed(arg_combinations)):
#        url_combination = url_partition[0] + url_partition[1]
#        for arg in arg_combination:
#            url_combination += arg + '&'
#        url_combination = url_combination[:len(url_combination) - 1]
#        generate_image(url_combination,
#                       path.join(path.realpath(path.dirname(__file__)),
#                                 "media/img%d.png" % i))

    # Calculate diff
#    hamming_distances = []
#    for i in range(len(arg_combinations)):
#        hamming_distances.append(imagediff('hamming',
#                                           'media/img0.png',
#                                           "media/img%d.png" % i))

#    print hamming_distances

if __name__ == '__main__':
    main('http://google.com/?name=me&where=here&when=now')
