'''
Part 1 :-
'''

# Answer 1.1 :-
'''
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

def my_median(ages):
    ages.sort()
    print('Sorted list:', ages)

    if len(ages)%2 == 0 :
        median_val_1 = int(len(ages)/2 - 1)
        median_val_2 = int(len(ages)/2)
        median_even_value = (median_val_1+median_val_2)/2
        print('Even value is : ',ages[median_even_value])
    else:
        median_odd_value = int((len(ages)+1)/2 -1 )
        print('Odd value is : ',ages[median_odd_value])

my_median(ages)

list_count = len(ages)-1
greater_average = round((list_count)*0.9)
print('Position of the greater value is: ',greater_average)
print('The age greater than 90% of the other ages is: ',ages[greater_average])
'''

#Answer 1.2 :-
'''
def sum_test(n):
    summation_val = 0
    for i in range(1,n+1):
        summation_val = summation_val+i
    print('The summation of the sequence of number',n,'is:',summation_val)

sum_test(12)

'''
#Answer 1.3 :-

'''
score = 0
while True:
    try:
        score = int(input('please_fill_your_score: '))
        if (score < 60):
            print('F')
            break
        elif (score >= 60 and score <70):
            print('P')
            break
        elif (score >= 70 and score <80):
            print('C')
            break
        elif (score >= 80 and score <90):
            print('D')
            break
        elif (score >= 90):
            print('HD')
            break
        else:
            ('Incorrect number!')
    except(ValueError,TypeError):
        print('Please enter only Integer Values please!')
    finally:
        pass

'''

#Answer 1.4 :-

# For Loop

'''

num = 5

for i in range(1,num+1):
    for j in range(1, i+1):
        print('*', end =" ") 
    print("")

for k in range(num-1,0,-1):
    for l in range(1,k+1):
        print('*', end=" ")
    print("")
'''

# While Loop
'''
num = 5

i=1
while num>0:
    while i<=num:
        j=1
        while (j<=i):
            print("*", end = " ")
            j+=1
        print("")
        i+=1
    break

k=1
while k<=num-1:
    l = num
    while l-1>=k:
        print("*", end = " ")
        l-=1
    print("")
    k+=1
'''

# Answer 1.5 :-

'''
def digits_in_string(string):
    new_string = ""
    for i in string:
        if i.isdigit():
            new_string+=i
            result = new_string
    print(result)

digits_in_string("aAsmr3idd4bgs7Dlsf9eAF")
'''

#Answer 1.6 :-

'''
def find_all(string, sstring):
    string_list = []
    string_length = len(string)
    string_index = 0

    while string_index < string_length:
        i = string.find(sstring,string_index)
        if i == -1:
            return string_list
        string_list.append(i)
        string_index = i+1
    return string_list

print(find_all('helloworldhelloPythonhelloc++hellojava','hello'))

'''

# Answer 1.7

'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('name: {} , age: {}'.format(self.name,self.age))

    def Set_Age(self,value):
        self.age = value
        print(self.age)

    def Get_Age(self):
        return(self.age)

    def Updated_name_age(self):
        print('name: {} , age: {}'.format(self.name,self.age))


obj_1 = Person('Daniel',50)

obj_1.Set_Age(60)
obj_1.Get_Age()
obj_1.Updated_name_age()
'''


# Answer 1.8

'''
def permute(nums, index_value=0):

        if len(nums)==1:
            print([nums])

        if len(nums)==0:
            return []

        if index_value == len(nums):
            print([nums], end = ",")
        else:
            for i in range(index_value, len(nums)):
                nums[index_value], nums[i] = nums[i] ,nums[index_value]
                permute(nums, index_value+1)
                nums[index_value], nums[i] = nums[i], nums[index_value]

nums = [1,2,3]
unique_nums = set(nums)

if len(unique_nums)==len(nums):     
    permute([1,2,3])
else:
    print('Enter only unique values!')

'''

# Part 2: -
'''
def sum_digits(n):
    r=0
    while n:
        r, n = r + n % 10, n // 10
    return r

def check_studentid(studentid): 
    x = sum_digits(studentid)
    if x % 2 == 0:
        print ('version I')
    else :
        print('version II ')

check_studentid (220156351)
#replace the value by your student ID
'''
#Version 2:-

# Answer 2: -
'''
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns



X=np.linspace(0, 3, 30)
Y = 2.5*np.linspace(0, 3, 30) + 5*np.random.rand(30)
fig, ax=plt.subplots() 
ax.set_title('Regression line to fit') 
ax. set_ylabel ('Y')
ax. set_xlabel ('X')
ax.plot(X, Y, label='line to fit')
ax . legend ()
plt .show()

def find_error(a,X,Y):
  y_fit = a*X
  mse = np.square(np.subtract(y_fit,Y)).mean()
  rmse = m.sqrt(mse)
  return rmse

def fit_regression(n,X,Y):
  a_adjust = np.array(np.linspace(0,3,n))
  a = a_adjust[0]
  error = find_error(a,X,Y)
  for i in a_adjust:
    error_new = find_error(i,X,Y)
    if error_new < error:
      a = i
      error = error_new
    #print(error)
    print(round(a,4))
  fig, ax=plt.subplots() 
  ax.set_title('Regression line to fit') 
  ax.set_ylabel ('Y')
  ax.set_xlabel ('X')
  ax.plot(X,Y,label='line to fit')
  #ax.plot(X,Y,'o',colour ='blue')
  ax.plot(X,a*X,label='fitted line') 
  ax.legend()
  plt.show()


n = 100000
fit_regression(n,X,Y)
'''