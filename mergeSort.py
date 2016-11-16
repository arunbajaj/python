def mergesort(a): 
    if len(a) == 1: 
        return a
        #calculate mid value
    m = len(a)/2

    #divide array into two parts and call mergeSort again recursive call
    l = mergesort(a[:m]) 
    r = mergesort(a[m:])
    sa = merge(l,r)

    return sa
    #print a1

def merge(l,r):
    """
        Merge two arrays
    """
    result = []
    nleft = len(l)
    nright = len(r)
    i, j, k = 0, 0, 0 
    #loop through lens of l and r
    while i < nleft and j < nright:
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1 
        k += 1
    #Copy remainging items of l first then r
    result += l[i:]
    result += r[j:]
    return result

#a = [1,3,5,2,4,6]
#a = [ 1, 53, 6, 23, 4]
a = [1, 19, 7, 2, 5, 25, 85, 3, 15]
print a
print mergesort(a)