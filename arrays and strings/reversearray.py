# reverse array in place

def reverse_array(lst):
    for i in range(0, len(lst)//2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
    return lst

# time complexity is linear O(n), as for loop repeats n/2 times
# space complexity is constant time O(1)
