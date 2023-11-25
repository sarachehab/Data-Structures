# find longuest subarray with sum less or equal than k

def check_sum_subarray(lst, k):
    left = 0
    current_sum = 0
    maximum_sum = current_sum

    for right in range(len(lst)):
        current_sum += lst[right]

        while current_sum > k:
            left -= 1
            current_sum -= lst[left]

        if maximum_sum < current_sum:
            maximum_sum = current_sum

    return maximum_sum

# linear time complexity O(n), pointers LEFT and RIGHT can only move n spots each -> maximum 2n
# amortized 0(1) inside for loop -> while loop runs maximum of n times

# constant space complexity O(n) -> longuest_subarray is saved, maximum length = n
