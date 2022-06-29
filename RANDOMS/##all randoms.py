
##choosing a color 
'''import random
color=(['red','blue','yellow','green','grey'])
colorr=input('entrr a color')
while color==colorr:
    colorr=input('entrr a color')
    print('you mustb be ', color, ' with envy')
    print(color)
input('try again ')
colorr=input('enter a color')
'''

##math quiz
import random
score =0
for i in range(1,6):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    correct=num1+num2
    print(num1, '+', num2, '=')
    answer=int(input('enter your answer'))
    print(answer)
    if answer==correct:
        score=score+1
print('you scored ', score, ' out of 5')




