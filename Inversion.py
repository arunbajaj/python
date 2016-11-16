 
def mergesort(a): 
    if len(a) == 1: 
        return (a,0)
        #calculate mid value
    m = len(a)/2

    #divide array into two parts and call mergeSort again recursive call
    (l, x) = mergesort(a[:m]) 
    (r, y) = mergesort(a[m:])
    (sa, z) = merge(l, r)

    return (sa, x + y + z)

    #print a1

def merge(l, r):
    """
        Merge two arrays
    """
    result = []
    nleft = len(l)
    nright = len(r)
    i, j, k = 0, 0, 0
    inversion = 0
    #loop through lens of l and r
    while i < nleft and j < nright:
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
            #inversion +=1
            inversion += (nleft-i) 
        k += 1
    #Copy remainging items of l first then r
    result += l[i:]
    result += r[j:]
    return (result,inversion)

#a = [1,3,5,2,4,6]
#a = [ 1, 53, 6, 23, 4]
#a = [1, 19, 7, 2, 5, 25, 85, 3, 15]
#print a
def readfiles(path):
    array = []
    with open(path) as f:
        for line in f:
            array.append([int(i) for i in line.split()]) 
    print len(array)
    return array

array = readfiles('IntegerArray.txt')
#array = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
#array = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
(sortedarray,numOfInversion) = mergesort(array)
print numOfInversion