import random
import time

number = input('How many number do you want to guess:')
number = int (number)

chack = []

for i in range (0,number):
    chack.append(random.randint(0,101))
print(chack)
time.sleep(0.7)
for i in range (0,50) :
        print('')
for i in range(0,number):
    print('enter number at index' +str(i))
    count= int (input())
    if count == chack [i]:
         print(('correct'))
    else:
         print('Worng')
         break
print(chack)