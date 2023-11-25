# maximum avg subarray of defined length k

def max_avg(lst, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += lst[i]
    max_sum = curr_sum

    for i in range(k, len(lst)):
        curr_sum += lst[i] - lst[i-k]
        max_sum = max(max_sum, curr_sum)

    return max_sum/k


lst = [7, 4, 5, 8, 8, 3, 9, 8, 7, 6]
print(sum(lst[0:7]))
k = 7

print(max_avg(lst, k))

# time complexity is O(n)
# space complexity is O(1)
