'''
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
1  2  3  4  5  6  7   8   9   10

Write a recursive function named fibo that accepts a positive integer nn as argument and returns the n^{th}n th
  Fibonacci number. For this problem, F_1 = F_2 = 1F 1 =F 2 =1 are the first two Fibonacci numbers.
'''
def fibo(n):
    """
    compute the nth fibonacci integer
	
    Argument:
        n: int
    Return:
        f_n: int
    """
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

# Mathemtical Formula for Fib Fn = Fn-1 + Fn-2


print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(10))
