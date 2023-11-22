# check if two items in ordered list add up to n

def checksum(lst, n):
    left_pointer = 0
    right_pointer = len(lst)-1

    while (left_pointer < right_pointer):

        sum_items = lst[left_pointer] + lst[right_pointer]

        if (sum_items == n):
            return True
        elif (sum_items < n):
            left_pointer += 1
        else:
            right_pointer -= 1

    return False


# algorithm time complexity is O(n) -> sum of pointer is always n = length of the list
# algorithm space complexity is O(1) -> only checking two values within list
