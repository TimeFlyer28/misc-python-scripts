
#Practice Library

#Thsi is the Library where i have all of my practice scripts to look at

import time



#Creates list of all playing cards


suits = ['Spades','Diamonds','Hearts','Clubs']
numbers = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']

for s in suits:
    for n in numbers:
        print(str(n) + ' of ' + s)


time.sleep(5.5)


#numbers doubled until 1024

number = 1

while number <= 1024:
    print(str(number))
    number=number*2


input('press enter to continue')




