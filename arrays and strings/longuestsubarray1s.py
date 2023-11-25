# find longuest subarray of 1s containing only 1 0

def find_length(s):
    left = 0
    nb_zero = 0
    max_length = 0

    for right in range(1, len(s)):

        if s[right] == '0':
            nb_zero += 1

        while nb_zero > 1:
            if s[left] == '0':
                nb_zero -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# time complexity is linear time O(n), since work inside for loop is amortized O(1)
# constant space complexity
