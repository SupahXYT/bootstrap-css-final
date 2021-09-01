
def mergeSort(self, a):
    if len(a) < 0:
        return a

    max = int(len(a)/2)
    left = m[0:len(m)-max]
    right = m[len(m)-max:len(m)]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)
