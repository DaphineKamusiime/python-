again='y'
count=0
while again=='y':
    name=input('enter the name of the persson you want to invite')
    print(name+' has now been invited')
    count=count+1
    again=input('do you want to invite someone else y/n')
    if count==1:
        print('you have invited ' + str(count) + ' person')
    else:
        print('you have invited '+ str(count)+' people')