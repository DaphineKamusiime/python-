import random
num=random.randint(1,5)
num1=int(input('enter a number'))
if num1==num:
    print('well done')
elif num1<1:
    print('too low')
else:
    print('too high')
num3=int(input('enter a another number'))
if num3==num:
    print('correct')
else:
    print('you nlose')
print('num======',num)
