'''
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). 
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.
'''

def factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i ==0:
            factors.append(i)
    return factors

def isprime(n):
    if factors(n) == [1,n]:
        	return True
    
def Twin_Primes(n,m):
    PrimesBetween=[]
    twinprimes=[]
    pair=()
    for i in range (n,m+1):
         if isprime(i):
              PrimesBetween.append(i)
    
    if len(PrimesBetween)>2:
        for i in range(len(PrimesBetween)-1):
            if  abs(PrimesBetween[i] - PrimesBetween[i+1] )== 2:
                pair = (PrimesBetween[i]) , (PrimesBetween[i+1])
                twinprimes.append(pair)

                 
    print(twinprimes)

n= 1 #int(input())
m= 5 #int(input())
#print(sorted(Twin_Primes(n, m)))
Twin_Primes(n,m)