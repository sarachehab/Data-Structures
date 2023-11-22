# merge and sort two arrays a1 and a2

def mergesort(a1, a2):
    i1 = 0
    i2 = 0
    sorted = []

    for i in range(len(a1)+len(a2)-1):

        if (i1 == len(a1)-1):
            sorted.append(a2[i2])
            i2 += 1
        elif (i2 == len(a2)-1):
            sorted.append(a1[i1])
            i1 += 1
        elif a1[i1] < a2[i2]:
            sorted.append(a1[i1])
            i1 += 1
        else:
            sorted.append(a2[i2])
            i2 += 1

    return sorted

# a1 has length n and a2 has length m
# linear time complexity of O(n+m) -> each iteration only moves one pointer forward
# space complexity is O(1)
