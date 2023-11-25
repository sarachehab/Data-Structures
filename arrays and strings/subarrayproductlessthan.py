# find the nb of subarrays where the products of the elements is less than k

def find_nb_subarrays(lst, k):
    left = 0
    nb = 0
    curr_product = 1

    for right in range(len(lst)):
        curr_product *= lst[right]

        while curr_product >= k:

            curr_product = curr_product / lst[left]
            left += 1

        nb += right - left + 1  # this is the number of valid windows ending at index right

    return nb


# algorithm is linear time O(1), since for loop is amortized O(1)
# algorithm has constant time complexity
