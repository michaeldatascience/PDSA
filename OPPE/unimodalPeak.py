def checkPeak(A,i):
    return A[i] > A[i-1] and A[i] > A[i+1]


def peak_unimodal(A):
    if len(A) < 3:
        return
    
    (left,right) = (0, len(A)-1)
    #print(f'left{left} right{right}')
    while right >= left:
        mid = (left+right)//2
        #print(f'left :{A[mid-1]} middle : {A[mid]}  right{A[mid+1]}')
        if checkPeak(A,mid):
            #print(f'found at {mid}')
            return mid
            
        if A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            #print(f'going up. left = {mid}')
            left = mid + 1
        
        if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
            #print(f'going down right= {mid}')
            right = mid -1

    return None

A = [2, 3, 4, 21, 43, 52, 51, 18, 11, 9, 6, 5, 1]
peak= peak_unimodal(A)
print(f'A: {A}')
print(f'Peak {A[peak]} at {peak}')