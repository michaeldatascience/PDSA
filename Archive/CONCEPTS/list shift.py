num =4
l1 = [1, 2, 3, 4, 5, 6] 

def shiftL(L,n):
    pivot = n % len(L)
    return (L[-pivot:] + L[:-pivot])


print(shiftL(l1,10))