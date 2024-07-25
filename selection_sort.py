# selection sorting algorithm
def selection_sort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l
