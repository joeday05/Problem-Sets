# Linear Search
def search(list, element):
    for e in list:
        if e == element: 
            return True
    return False


# Linear Search using Recursion
def rSearch(list,element):
    if element == list[0]:
        return True
    if len(list) == 1:
        return False
    return rSearch(list[1:],element)


# Binary Search using Recursion
def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list)/2
    if list[mid] > element:
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        return rBinarySearch( list[mid : ] , element)
    return True


# Binary Search using Recursion
def search2(L, e):
    def bSearch(L, c, low, high):
        if high == low:
            return L[low] == c
        mid = low + int((high - low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid)
        else:
            return bSearch(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) -1)
        

        