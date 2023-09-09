'''
Swapping Min-max
You are given two lists a and b of n positive integers each. You can apply the following swap operation to them any number of times:
Select index i (0 < i < n-1) and swap ai with bi (i.e. ai becomes bi and vice versa).
Write a function minmax(a, b) which takes two lists a and b of size n as inputs and returns an integer, which is the minimum
possible value of max (ao, a1 .., an-1) X max(b0, b1, . ..,bn-1) you can get after applying the swap operation any number of
times (possibly zero).
Example
Consider the lists - a = [1,2,6,5, 1,2] and b = [3,4,3,2,2,5]
In this case, you can apply the swap operation at indices 1 and 5, then a = [1,4,6,5,1,5] and b = [3,2,3,2,2,2] and
max (1, 4, 6, 5, 1, 5) x max (3, 2, 3, 2, 2, 2) = 6 x 3 = 18
Sample Input 1
[1,2,6,5,1,2]
[3,4,3,2,2,5]
Output
18
Sample Input 2
[3,3,3]
[3,3,3]
Output
9
'''


def minmax(a,b):
    size = len(a)
    for i in range (len(a)):
        #print(f'i{i} a[i]{a[i]}')
        if a[i]<b[i]:
            #print (f'swapping')
            (a[i],b[i]) = (b[i],a[i])
    maxa= max(a)
    maxb= max(b)
    #print(f'maxa :{maxa}')
    #print(f'maxb :{maxb}')
    
    return maxa*maxb
    
#a = eval(input())
#b = eval(input())
a=[1,2,6,5,1,2]
b=[3,4,3,2,2,5]

print(minmax(a,b))