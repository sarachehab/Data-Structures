# ordered array out of squares of a

def square_array(a):
    negative_dir = 0
    positive_dir = len(a)-1

    out = [0]*len(a)

    for i in range(len(a)-1, -1, -1):

        # biggest abs values means biggest square
        if abs(a[negative_dir]) > abs(a[positive_dir]):
            out[i] += a[negative_dir]**2
            negative_dir += 1
        else:
            out[i] += a[positive_dir]**2
            positive_dir -= 1

    return out

# time complexity is linear time O(n), as we are iterating through whole array
# space complexity is constant O(1), O(n) if output is taken into consideration
