# Write code here
AmountList=[]   # Global List

def checkAmt(L):
    print (f'Last:{L[-1]} - First:{L[0]} = {L[-1] - L[0]}')
    return L[-1] - L[0]

def rotateAndCheck(L,skip):
    # skip: how many to skip from left
    print(f'Inital: {L}, skip:{skip}')
    iList = L[skip:]
    for i in range(len(iList)):
        iList = rotateRight(iList)
        skipped = L[0:skip]
        combined = skipped + iList
        print(f'Rotated List{iList}: Skpped List{skipped} : combined:{combined}' )
        
        AmountList.append(checkAmt(combined))

    print(f'AmountList: {AmountList}')

def rotateRight(L):
    rotated=[]
    rotated.append(L[-1])
    for i in range (len(L)-1):
        rotated.append(L[i])
    
    
    return rotated

def Max_Amount(a):
# Write code here   
    L=[]
    
    # First rotate the list and store all amount without skipping
    #rotateAndCheck(L,0)
    for i in range(len(a)):                   
        rotateAndCheck(a,i)                  

    print(AmountList)
    print(max(AmountList))


    
# Suffix Code( Don't remove)
a = [6, 10, 2, 5, 10, 3, 1, 9, 10, 10]
print(Max_Amount(a))