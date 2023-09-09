''' 
Goldbatch conjencture
Every number > 2 is a sum of prime
e.g. 
7 -> (5,2)
12-> (5,7)
26-> (7,19) (3,23) (13,13)
'''
def factors(n):
    result=[]
    for i in range(1,n+1):
        if n%i ==0:
            result.append(i)
    return result

def isprime(n):
    if factors(n)==[1,n]:
        return True
    else:
        return False

def goldbatch(n):
    factors=[]
    for i in range (2,n+1):
        if isprime(i)== True:
            for j in range (i,n+1):
                if isprime(j)== True:
                    if i+j==n:
                        print(f'i:{i} j:{j}={i+j}')
                        factorSet=(i,j)
                        factors.append(factorSet)
    return factors

print(goldbatch(26))
