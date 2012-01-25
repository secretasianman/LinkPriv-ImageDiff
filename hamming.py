def hamming_distance(string1, string2):
    return sum(1 if i != j else 0 for i, j in zip(string1, string2))
