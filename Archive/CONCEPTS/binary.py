
#L = [print(x) for x in range(10)]
#print (L)

def binary_search(L,n, left=0, right=0):
    if left==0 and right==0: # initial setup
        left=0
        right=len(L)

    midIndex = len(L)//2 #(left+right)//2
    mid = L[midIndex]
    if mid==n:
        return True
    else:
        if n > mid:
            left=midIndex
        else:
            right=midIndex
        
        binary_search(L[left:right],n,left,right)



L=[12,20,35,5,54,60,95,21,75,8,100,18,24]
L = sorted(L)
print(binary_search(L,54))


'''
[1,3,5,7,9,10,13,16,30] 7

left=1, right=30


'''