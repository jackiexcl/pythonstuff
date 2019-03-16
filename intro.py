# use python filename.py to run file in terminal


#### CHAPTER 1 INTRODUCTION ########
# Indentation matters in python
# user \ to move on to next line 
# exponent **
# remainder %
# floored quotient //
# division /
# multiply *

# integer
# int() converts into integer form
y = 2
global x

# floating point
# float() converts into float form
x = 2.5

# string 
# str() converts into string form
z = 'Hello'

z1 = 'World'

#contanate into Hello World， ＋ is for concantenate
zz1 = z+z1  
#print(zz1)

#input function for user to key in. use raw_input
#print('please type in your name')
myname = raw_input()
#print ('your name is '+ myname)

# len() returns length
namelength = len(myname)
#print ('length of name is '+ namelength)

# ###### CHAPTER 2 FLOW CONTROL $$$$$$$$$
# BOOLEANS
# == equal to
# != not equal to
# < less than, <= less than equal to
# > greater than, >= greater than equal to
# and, or, not 
outcome = (3>1) and (4>2) # evaluates to true
# print(outcome)

## if statements
# if outcome == True :
# 	print ('it is true')
# elif: outcome == False;
# 	print ('it is false')
# else:
# 	print ('no answer')


## while loops
# while True:
#   print('Who are you?')
#   name = input()
#   if name != 'Joe':       #(1)
#     continue              #(2) # continue acts as intermediate check
#   print('Hello, Joe. What is the password? (It is a fish.)') 
#   password = input()      #(3)
#   if password == 'swordfish':
#     break                 #(4) # breaks out of the loop
# print('Access granted.')  #(5)

## for loops
# to sum from 1 to 101
# total = 0               #(1)
# for num in range(101):  #(2)
#    total = total + num  #(3)
# print(total)            #(4)

# for loop with a range
# for i in range(0, 10, 2):
#     print(i)

## importing library
# import random
# for i in range(5):
#     print(random.randint(1, 10))

## to exit a program
# import sys
# sys.exit()


####### CHAPTER 3 FUNCTIONS #######

# creating a function 
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
 # calling function 
hello()

# creating a function with inputs
def hello(name):
   	print('Hello ' + name)

hello('Alice')
hello('Bob')


# returning a value to the function 
def getAnswer(answerNumber):
    if answerNumber == 1:
           return 'It is certain'
    elif answerNumber == 2:
           return 'It is decidedly so'
    elif answerNumber == 3:
           return 'Yes'

# None is null in Python

# putting global in front of a variable makes it global variable


######### CHAPTER 4 LISTS ########
# using negative index spam[-1] means the last item
spam = ['cat', 'bat']
# can use del spam[2] to delete 2nd item 

'hi' in ['hello', 'hi', 'whatsup'] # returns true
# can also use not in

# ListName.index(itemName) returns index of item
# Can use ListName.append(itemName) and ListName.insert(itemName) to add items to a list
# Can use ListName.remove(itemName) to remove the item
# ListName.sort() will sort the list by order
# ListName.sort(reverse=True) will sort in reverse order

# tuples are ummutable lists, and they use parenthesis
# tupleName = ('cat', 'mouse')
# use CopiedList = copy.copy(OriginalList) to make a copy of the list
# in Python, the reference is passed around, and original list will be modified
# copy.deepcopy will apply to lists with inner lists


########## CHAPTER 5 DICTONARY (KEY-VALUE PAIRS) ########









