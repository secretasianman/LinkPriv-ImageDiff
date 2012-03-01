def levenshtein_distance(string1, string2):
    m = len(string1)
    n = len(string2)
    distance = [[float("inf") for i in range(n + 1)] \
                    for j in range(m + 1)]
    for i in range(m):
        distance[i][0] = i
    for j in range(n):
        distance[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = min(distance[i - 1][j] + 1,
                                     distance[i][j - 1] + 1,
                                     distance[i - 1][j - 1] + 1)
                
    return distance[m][n]
