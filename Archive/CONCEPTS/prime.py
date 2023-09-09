def isprime(n):
    result=True
    if n==1:
        return False

    for i in range(2,n):
        if n % i ==0:
            result = False

    return result
      

def prime_produt(n):
    result = False
    for i in range (2,n):
        if isprime(i):
            for j in range(2,n):
                if isprime(j):
                    k = i*j
                    print(f'i={i} & j={j}: i*j={k}')
                    if k==n:
                        result = True
        
    return result



#Suffix Code
#n = int(input())
#print(isprime(8))
print(prime_produt(12))

#for i in range (1,100):
#    if (isprime(i)):
#        print(i, end=",")