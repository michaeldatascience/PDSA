# Write your code here

def binSearch(e,L):
  #return pos of e in L using bin search
  if len(L)==0:
    return -1

  left,right = 0,len(L)-1
  while right>=left:
    mid =(left + right) // 2
    if L[mid] == e:
      return mid

    if  e > L[mid]:
      left = mid -1

    if e < L[mid]:
      right = mid + 1

    return -1
    
def findCommonElements(A, B):
  # traverse through A
  # search every element of A in B using bin search
  # return the result
  A.sort()
  B.sort()
  C = []
  foundPos = -1
  for i in range(len(A)):
    foundPos = binSearch(A[i],B)
    if foundPos > 0:
      C.append(A[i])
    
  return C

# Suffix code
#A = eval(input())
#B = eval(input())
A = [3, 7, 2, 9, 5]
B = [6, 3, 7, 5, 4]

result = findCommonElements(A, B)
result.sort()
print(result)
