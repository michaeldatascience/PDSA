def ShiftTop(Q, token):
    print(f'Q = {Q} token={token}')
    Q.insert(0,token)
    print(f'after insertion{Q}')

def Join(Q,token):
    Q.append(token)

def Leave(Q):
    Q.pop(0)

def Print(Q):
    print(Q)

def Move(Q,token,location):
    print(f'Move {token} to {location} ')
    if location=='HEAD':
        Q.remove(token) 
        #MoveTop(Q,token)
        Q = ShiftTop(Q,token)
    else:
        Q.remove(token)
        Q.append(token)



Q=[]
inputText = ''

'''
while(inputText!='END'):
    inputText = input()
    inputL = inputText.split(',')
    if (inputL[0]=='JOIN'):
        Join(Q,inputL[1])
        
    elif (inputL[0]=='LEAVE'):
        Leave(Q)
        
    elif (inputL[0]=='MOVE'):
        Move(Q,inputL[1],inputL[2])
        
    elif (inputL[0]=='PRINT'):
        Print(Q)
    
'''    

'''
JOIN,1
JOIN,2
JOIN,3
PRINT
MOVE,3,HEAD
PRINT
END
1,2,3
3,1,2

'''

Join(Q,1)
Join(Q,2)
Join(Q,3)
Print(Q)
Move(Q,3,'HEAD')
Print(Q)
