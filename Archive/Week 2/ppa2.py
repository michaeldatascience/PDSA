# len(L) = n
# Li ~[0,r)
#n>>r
# L= 2,0,1,1,2,3,0,2,1,0,2,3,1,2
# r = 4

def sortInRange(L, r):
    





def sortInRange2(L, r):
    d = {}       
    for j in L:
        if j in d:
            d[j]+=1
        
        else:
            d[j] = 1
        
    L.clear()
    
    for i in range(r):
      for j in range(d[i]):
        L.append(i)
L = [int(item), for item in input().split()]  
r = int(input())
print(L)