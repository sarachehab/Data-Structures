# find longuest subarray with a maximum of k 0s

def find_length(lst, k):
    left = 0
    nb_zeros = 0
    max_length = 0

    for right in range(len(lst)):

        if lst[right] == 0:
            nb_zeros += 1

        while nb_zeros > k:
            if lst[left] == 0:
                nb_zeros -= 1
            left += 1

        max_length = max(max_length, 1 + right - left)

    return max_length


# time complexity is O(n), since right and left span n each
# space complexity is constant O(1)
