'''
a=input("enter a")
b=input("enter b")
sum=int(a)+int(b)
print(sum)
quotient=int(a)/int(b)
print(quotient)
print(f"{quotient:.2f}")
'''
'''
firstname=input("enter first name")
secondname=input("enter second name")
#name= str(firstname)+str(secondname)
print(len(firstname))
print(len(secondname))
print(firstname.title())

#print(name.upper())
print(str(firstname).upper(), str(secondname).upper(), sep=" ")


x=0
while x<5:
    print("wowwwwwwwwwww")
    x=x+1'''
'''
names=['daphyne','hassan','nabil']
print(names[-1])
print(names[0])
print(names[-2])
print(names[0].upper())
print(names[0:3])

mycar={'color':'black matte','size':'medium','type':'mercedes'}
print('my car is '+mycar['color'])
print('it is '+mycar['size']+' sized')

def name():
    name=input('name...')
    print(name)
print('sdfghj')
name()
'''
'''

spam={'color':'red','age':'42','colour':'blue'}
spam['color']='yellow'
spam.setdefault('color','yellow')
spam['age']='32'
spam.setdefault('age','32')
for i in spam.items():
    print(i)

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

schoollist={'books':'6','pens':'8','bag':'1'}
print('i need '+str(schoollist.get('bag',0))+' bag'
+', '+ str(schoollist.get('pens',0))+' pens'
+' and '+str(schoollist.get('books',0))+' books')


message='i love playing chess and eating icecream'
count={}
for character in message:
    count.setdefault(character, 0)
    count[character]=count[character]+1
    print(count)'''

'''
##001 ###002
firstname=input("enter your firstname")
secondname=input("enter your secondname")
name=str(firstname)+str(secondname)
print("hello " + firstname.upper())
print("hello "+ firstname.title()+' '+ secondname.title())

###003
print('what do you call a bear with no teeth\n A gummy bear')

###004 ###005
firstnum=int(input('enter first number'))
secondnum=int(input('enter second number'))
sum=firstnum+secondnum
print(sum)
thirdnum=int(input('enter third number'))
result=sum*thirdnum
print(result)
###006
initial=int(input('how many slices of pizza did you start with'))
final=int(input('how many slices have you eaten'))
left=initial-final
print('you are left with '+ left)
###007
age=int(input('enter your age'))
new=age+1
name=str(input('enter your name'))
print(name+'next birthday you will be '+ str(new))

###008
bill=int(input('what is your total bill'))
number=int(input('how many diners'))
result=bill/number
print('each person will pay '+str(result))

#009
days=int(input('enter number of days'))
hours=24*days
minutes=60*24*days
seconds=60*60*24*days
print(str(hours) + 'hours')
print(str(minutes) + 'minutes')
print(str(seconds) + 'seconds')

###010
weight_in_kilos=int(input("enter weight in kilos"))
weight_in_pounds=int(2204*weight_in_kilos)
print(weight_in_pounds)


###011
firstnum=int(input('enter a number greater than 100'))
secondnum=int(input('enter a number less than 10'))
result=firstnum/secondnum
print(firstnum ,'goes into ', secondnum, ' ' ,result,' times')


###012
firstnum=int(input('enter first number'))
secondnum=int(input('enter second number'))
if firstnum>secondnum:
    print(secondnum,firstnum)
else:
    print(firstnum,secondnum)

###013
num=int(input('enter a number'))
if num>=20:
    print('TOO HIGH')
else:
    print('thanks')

    ###014
    x=int(input('enter number between 10 and 20 inclusive'))
if x >=10 and x<=20:
    print('............')
else:
    print('out of range')


    ###015
color=input('what is your favourite color')
if color=='red' or color=='RED' or color=='red':
    print('i love red too')
else:
    print('i prefer red')

###016
reply=input('is it raining')
print(reply.lower())
if reply=='yes':
    reply_two=input('is it windy')
    if reply_two=='yes':
        print('it is too cold for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')


###017
age=int(input('what is your age'))
if age>=18:
    print('you can vote')
elif age == 17:
     print('you can learn to drive')
elif age == 16:
    print('you can buy a lottery ticket')
else:
    print('you can go trick-or-treating')


###018
a=int(input('enter a number'))
if a<10:
    print('too low')
elif a<20 and a>10:
    print('correct')
else:
    print('too high')


###019
x=int(input('enter 1, 2, or 3'))
if x==1:
    print('thank you')
elif x==2:
    print('well done')
elif x==3:
    print('correct')
else:
    print('error')

###020,021,022
name_first=input('enter your firstname')
print(len(name_first))
name_sur=input('enter sur name')
print(name_first+' '+ name_sur)
name=name_sur+' '+name_first
print(len(name))
print(name.upper())


###023.###024
rhyme=input('enter nursery rhyme')
print(len(rhyme))
start=int(input('enter a beginning number'))
end=int(input('enter an ending number'))
print(rhyme[start:end])
print(rhyme.upper())


###025
name=input('enter your name')
if len(name)<5:
    surname=input('enter your surname')
    nAme=name+surname
    print(nAme.strip().upper())
else:
    print(name.lower())

word=input('enter a word')
first=word[0]
length=len(word)
rest=word[1:length]
if first=='a' or first =='e' or first=='o' or first=='i' or first=='u':
    piglatin=word+'way'
    print(piglatin)
else:
    piglatin=rest+first+'ay'
    print(piglatin)

###027,028
a=float(input('enter decimal'))
result=a*2
print(result)
print(f"{result:.2f}")

###029
x=int(input('enter an integer greater than 500'))
answer=x**0.5
print(answer)
print(f"{answer:.2f}")

###030,031,032
pi=22/7
print(pi)
print(f"{pi:.2f}")

radius=int(input('enter radius of a circle'))
area=pi*radius**2
print(area)
print(f"{area:.2f}")

radius_cy=int(input('enter radius of cylinder'))
depth=float(input('enter depth of the cylinder'))
area_cy=pi*radius**2*depth
print(area_cy)
print(f"{area_cy:.3f}")

###033
firstnumber=int(input('enter first number'))
secondnumber=int(input('enter second number'))
result=firstnumber//secondnumber
remainder=firstnumber-(secondnumber*result)
print('answer is '+str(result))
print(str(remainder) + ' is the remainder')

###034
print('1)Square\n 2)Triangle')
num=int(input('enter a number'))
if num==1:
    side=input('enter length of one side')
    area_s=int(side)**2
    print(area_s)
elif num==2:
    base=int(input('enter value of the base'))
    height=int(input('enter value of height'))
    area=0.5*height*base
    print(area)
else:
    print('enter 1 or 2')

###035,036
name=input('enter your name')

for i in range(0,3):
    print(name.upper())
   

###037
name=input('enter your name')
num=int(input('enter a number'))
for i in range(0,num):
    print(name.upper())
 
    ###038
name=input('enter your name')
num=int(input('enter a number'))
for i in range(0,num):
    for i in name:
        print(i)

###039
num=int(input('enter a number between 1 and 12'))
for i in range(1,12):
    print(num*i)

###040
num=int(input('enter number below 50'))
for i in range(num,50):
    print(i)

###041
name=input('enter your name')
num=int(input('enter a number'))
if num<10:
    for i in range(0,num):
        print(name)
else:
    print('too high')
    for i in range(0,3):
        print(name)

###042
total=0
for i in range(0,5):
    num=int(input('enter number'))
    ans=input('do u want this number to be included,,,,,yes or no')
    if ans=='yes':
       total=total+num
       print(total)
'''
###043
order=input('which direction do you want to count up or down')

if order=='up':
    topnum=int(input('enter top number'))
    for i in range(topnum,20):
        print(i)
elif order=='down':
    downnum=int(input('enter botton num'))
    for i in range(downnum,1):
        print(i)
else:
    print('i dont understand')




























































































































