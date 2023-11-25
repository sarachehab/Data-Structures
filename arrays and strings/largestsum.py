# find largerst sum of subarray of fixed length k

def largest_sum(lst, k):

    curr_sum = 0
    for i in range(k):
        curr_sum += lst[i]
    max_sum = curr_sum

    for i in range(k, len(lst)):
        curr_sum = curr_sum - lst[i-k] + lst[i]
        max_sum = max(max_sum, curr_sum)

    return max_sum


# linear time O(n), since we need to go through n-k iterations through for loops
# constant space complexity
