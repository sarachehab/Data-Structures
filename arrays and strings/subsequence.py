# decide if subsquence is in string s

def contains_subsequence(s, subsequence):
    i_string = 0
    i_subsequence = 0

    while i_string < len(s) and i_subsequence < len(subsequence):

        if (s[i_string] == subsequence[i_subsequence]):
            i_subsequence += 1

        i_string += 1

    return (i_subsequence == len(subsequence))


# algorithm time complexity is linear time O(n), where n is the length of the string s -> we are iterating through all n characters of s
# algorithm space complexity is O(1)
