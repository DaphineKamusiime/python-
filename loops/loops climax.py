'''
num=int(input('enter a number between 10 1nd 20'))
while num<10 or num>20:
    if num<10:
        print('too low')
    else:
        print('too high')
    num=int(input('try again'))
print('thank you')
        
  '''
numb=10
while numb>0:
    print(numb, " green bottles hanging on the wall ",numb, " green bottles on hanging on the wall " )
    answer=int(input('if one bottle falls,how many will be left'))
    newnumb=numb-1
    if answer==newnumb:
        print('there will be ',newnumb,' bottles left')  
    else:
        while answer!=newnumb:
            print('try again')
print('there are no more green bottles...')  
  
  
       
        
        