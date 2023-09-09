def binarySearch(L,k, left, right,recursionCount=0):
    if left > right:
        return(False,recursionCount)
    
    recursionCount +=1
    mid= (left+right)//2
    if k == L[mid]: # base case
        return(True,recursionCount)
    
    elif L[mid] < k:
        return(binarySearch(L,k,mid+1,right,recursionCount))
    elif L[mid] > k:
        return(binarySearch(L,k,left,mid-1,recursionCount))
    


def binarSearchIndexAndComparisions(L,K):
    result = binarySearch(L,K,0,len(L)-1)
    return result


L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]

print(binarSearchIndexAndComparisions(L,100))
"""
def binarySearch(L,k, c=0, resultL=[] ):
    # L- list
    # n- to search
    # start, stop list index
    # c- # comparisions
    n = len(L)
    if n > 1:
        mid = n//2
        c+=1
        
        if k==L[mid]:
            resultL.append((True,c))
            return
        elif k > L[mid]:
            binarySearch(L[mid:],k,c,resultL)
        elif k < L[mid]:
            binarySearch(L[:mid],k,c,resultL)
        
        resultL.append((False,c))
        return (resultL)
    
def binarySearchIndexAndComparisons(L,K):
    result = binarySearch(L,K)
    return(result[0])
    

L=[2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]

print(binarySearchIndexAndComparisons(L,11))
"""