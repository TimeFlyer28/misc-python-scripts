
import random

#average list

my_list = [5, 10, 15]

def avg_list(list_param):
    a = 0
    b = len(my_list)
    for x in list_param:
        a = a + x
    print(a/b)


#________________________________________________________________________


#Dictionary


#b = 5

#My_Dict = {'name':'Bob', 'lives':10}

#print(My_Dict["name"])

#print(My_Dict["lives"])

#My_Dict['lives'] = My_Dict['lives'] - b

#print(My_Dict['lives'])



def chance_generator(chance_list):

    global Yes_No
    
    Yes_No = random.choice(chance_list)



Death = [0, 0, 1]

chance_generator(Death)

print(Yes_No)