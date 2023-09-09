# write your code here
def find_kth_largest(T,k):
    root = T
    L=[]
    while (root.right):
        print(root.value)
        L.append(root.value)
        root = root.right
        
    L.reverse()
    kthitem = L[k:k+1]
    print (kthitem)






# Suffix Code
class Tree:
# Constructor:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return
    # Only empty node has value None
    def isempty(self):
        return (self.value == None)

    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return    

            

T = Tree()
bst = [1, 2, 3, 4, 5, 6, 7, 8, 9] #eval(input())
k = 3
for i in bst:
    T.insert(i)
print(find_kth_largest(T,k))