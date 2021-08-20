
import helper as h
def average(q,w):   
    #print("received var1 = "+str(q)) 
    #print(f"recevied var2 = {w}")
    z = q+w
    avg_value = z/2
    print(f"Average of {q} and {w} is equal to {avg_value}")
    checkGreaterThan100(avg_value)
    return

def checkGreaterThan100(a):
    if(a>100):
        print(f"{a} is greater than 100")
    else:
        print(f"{a} is less than 100")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def my_sum(my_list_param):
    s = 0
    for x in my_list_param:
        if(x%2 == 0):
            print(f"element x is {x}")
            print(f"element s is {s}")
            print(f"{x} is even number")
            s = s+x
            print(f"element s after s + x =   {s}")
    print(f"\n Sum of  elements in the list is {s}")


print("aaaaaaaa")


#average(20, 40)
#print("\n")
my_sum(my_list)


my_dict = { 'name': 'anish',
            'age': '10',
            'grade':'8',
            'school':'ardrey Kell' }

my_students_list = [ { 'name': 'anish', 
            'age': '16',
            'grade':'11',
            'school':'ardrey Kell'},
            { 'name': 'bob', 
            'age': '9',
            'grade':'4',
            'school':'elonpark'},
            { 'name': 'joe', 
            'age': '13',
            'grade':'8',
            'school':'community house' }
            
            
               ]

print(f"{my_dict['name']} is of age {my_dict['age']} he is in grade {my_dict['grade']} and going to school {my_dict['school']}")


#checkGreaterThan100(10)

#print("Average value is "+ str(avg))

#List Comprehension

num = [1,2,3,4,5,6,7,8,9,10]

"""
for n in num:
    k = n*n 
    print(k)

    """

new_list = [n*n for n in num]

#tuple

tp = (1, 2, 3)

print(tp)



