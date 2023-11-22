# check if string is palyndrome

def palyndrome(s):

    left_pointer = 0
    right_pointer = len(s) - 1

    while (left_pointer < right_pointer):

        if (s[left_pointer] != s[right_pointer]):
            return False

        left_pointer += 1
        right_pointer -= 1

    return True


# condition in while loop checked n/2 times
# algorithm time complexity is O(n)
# algorithm space complexity is O(1) -> only checking two values
