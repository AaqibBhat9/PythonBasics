#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:



mylist = ['apples', 'banana', 'grapes']
print(mylist)
print(len(mylist))


# # Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# 

# In[ ]:


list1 = ['abc', 11, True, 40]
print(type(list1))


# # The list() constructor
# it is also possible to use list() constructor when creating a new list

# In[ ]:


thislist = list(('string', 1, 'another string', 1, 'etc etc'))#note the double brackets
print(thislist)


# # Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# 
# -List is a collection which is ordered and changeable. Allows duplicate members.
# -Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# -Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# -Dictionary is a collection which is ordered** and changeable. No duplicate members.

# # Python Access List items

# In[ ]:


list = ['apple', 'banana', 'orange']
print(list[1]) #prints first element
print(list[-1])#-1 refers to last element and -2 refers to 2nd last and so on


#    # Range of indexs

# In[ ]:


list = [1,2,5,8,9,11,17]
print(list[1:4])#it will include first but not the last
print(list[:4]) #means from index 0 to 4 but 4 not included
print(list[2:]) #starts from 2 upto last index 
print(list[-4:-1]) 


# # check if item exists in list

# In[ ]:


list = ['apple', 'mango', 'grapes']
if 'apple' in list:
    print("Yes, 'apple' is in the list")
else:
    print("NO!!!")


# # Change item values

# In[ ]:


list = [1,2,3,4,5,6,7,8,9]
print("before changing the list element",list)
list[1]= 0
print("After changing the list element",list)
list[1:4] = 99,0
print(list)


# # to insert new item without replacing any existing element we can use insert() method

# In[ ]:


list = [1,2,3,4,5,6,7,8,9]
print(list)
print("Length before: ",len(list))
list.insert(0,100) #first one is index and second is value to be added in the list
print(list)
print("Length after: ",len(list))


# # Append Items

# In[ ]:


list = ['apple', 'banana', 'orange']
print("Before append",list)
list.append('grapes')
print("After append, it add item to the end of the list",list)


# # Insert Items
# To insert a list item at a specified index, use the insert() method.
# 
# The insert() method inserts an item at the specified index:

# In[ ]:


list = [0,1,2,3,4,5,6,7,8]
list.insert(0,100)
print(list)


# # Extend List
# To append elements from another list to the current list, use the extend() method.

# In[ ]:


list = [1,2,3,4,5,6]
list2 = ['one', 'two', 'three']
list.extend(list2)
print(list)


# # Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# In[ ]:


list = ['a', 'b', 'c']
thistuple = (1,2,3)
list.extend(thistuple)
print(list)


# # Remove Specified Item

# In[ ]:


list = ['a', 'b', 'c']
list.remove('b')
print(list)


# In[ ]:


list = ['a', 'b', 'c']
list.pop(0)
print(list)


# In[ ]:


lists = ['a', 'b', 'c']
lists.pop()
print(lists)


# # Loop Through a List
# You can loop through the list items by using a for loop:

# In[ ]:


thislist = [1,2,3,4,5,6,7,8]
for x  in thislist:
    print(x)


# In[ ]:


thislist = [1,2,3,4,5,6,7,8]
for i in range(len(thislist)):
    print(thislist[i])


# In[ ]:


thislist = [1,2,3,4,5,6,7,8]
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1


# # Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:

# In[ ]:


thislist = [1,2,3,4,5,6,7,8]
[print(x) for x in thislist]


# # List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# 
# Example:
# 
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# 
# Without list comprehension you will have to write a for statement with a conditional test inside:

# In[ ]:


fruits = ['apple', 'banana', 'grapes', 'kiwi', 'orange', 'mango']
newlist = []
for x in fruits:
    if'a' in x:
        newlist.append(x)
print(newlist)


# In[ ]:


fruits = ['apple', 'banana', 'grapes', 'kiwi', 'orange', 'mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist)


# In[ ]:


newlist = [x for x in range(10)]
print(newlist)


# In[ ]:


new = [x for x in range(10) if x<5]
print(new)


# In[ ]:


newlist= [x for x in fruits if x!= 'apple']
print(newlist)


# In[ ]:


newlist = [x.upper() for x in fruits]
print(newlist)


# In[ ]:


newlist =['hello' for x in fruits]
print(newlist)


# In[ ]:


newlist = [x if x!= 'banana' else 'orange' for x in fruits]
print(newlist)


# # Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# 
# 

# In[ ]:


thhislist = ['orange', 'apple', 'grapes', 'kiwi']
thhislist.sort()
print(thhislist)


# # sort descending
# use keyword reverse= true to sortr des

# In[ ]:


thhislist = [1,2,5,3,12,4,5]
thhislist.sort(reverse = True )
print(thhislist)


# In[ ]:


def myfunc(n):
    return abs (n - 50)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)


# # Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# 
# There are ways to make a copy, one way is to use the built-in List method copy().

# In[ ]:


thislist = ['a', 'b', 'c']
mylist = thislist.copy()
print(mylist)


# In[ ]:


thislist = ['a', 'b', 'c']
mylist = list(thislist)
print(mylist)


# # Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# 
# One of the easiest ways are by using the + operator.

# In[ ]:


list1 = [1,2,3,41]
list2 =['a', 'b', 'c']
list3 = list1 + list2
print(list3)


# In[ ]:


list1 = [1,2,3,41]
list2 =['a', 'b', 'c']

for x in list2:
    list1.append(x)
print(list1)


# In[ ]:


list1 = [1,2,3,41]
list2 =['a', 'b', 'c']
list1.extend(list2)
print(list1)


# # List Methods
# Python has a set of built-in methods that you can use on lists.
# 
# Method	       Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# In[ ]:


l1 = [1,2,4,1,3,4,6,2,4,6,7,2,1,233,4,6,2,1,2,3,54,21,1,3,5,6]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)
print("Prints unique numbers ")


# # eg2 fund sum of all numbers in list

# In[ ]:


l1 = [1,3,4,6,3,2,4]
total = 0;
for x in l1:
    total = total + x
print("Sum of all numebers using loop: ",total)

total = sum(l1)
print("Sum of all numbers sum() function :", total)


# # list of 5 random integers

# In[ ]:


import random
l1 = []
for i in range(5):
    x = random.randint(0,100)
    l1.append(x)
print(l1)


# # Tuple is one of the built-in data types in Python. A Python tuple is a sequence of comma separated items, enclosed in parentheses (). The items in a Python tuple need not be of same data type.
# 
# In Python, tuple is a sequence data type. It is an ordered collection of items. Each item in the tuple has a unique position index, starting from 0.
# 
# Python tuple and list both are sequences. One major difference between the two is, Python list is mutable, whereas tuple is immutable. Although any item from the tuple can be accessed using its index, and cannot be modified, removed or added.tuple is an immutable data type. An immutable object cannot be modified once it is created in the memory.
# 

# In[ ]:


tup1 =('abc', 123, 32, True)
print(tup1)


# In[ ]:


tupp1 = [1,2,4,5,7,3,2,45]
tup2 = ['a','abc', 'def']

print("Item at 0th index in tup1 :", tupp1[0])
print("Item at 2nd index in tup1 :", tup2[2])


# In[ ]:


tupl1= [22.22, 3.4, 52,55,223,4,52,3,4,2]
print("Items form index 0 to 4 :", tupl1[0:4])
print("Items form index 1 to 3 :", tupl1[1:4])
print("Items form index 0 to 4 :", tupl1[0:4])


# # how to update tuple

# In[ ]:


tup1 = ('a', 'b', 'c', 'd')
print("tuple before update :", tup1, "id():", id(tup1))

list1 = list(tup1)
list1[2] = 'f'
list1.append('z')
list1.sort()
print("updated list ", list1)

tup1 = tuple(list1)
print("tuple after update :", tup1, "id():", id(tup1))


# # unpacking tuples
# The term "unpacking" refers to the process of parsing tuple items in individual variables. In Python, the parentheses are the default delimiters for a literal representation of sequence object.

# In[ ]:


tup1= (10,20,50)
x, y, z = tup1
print("x:", x ,'Y:',y ,'Z :',z)
#x,y = tup1 shows error
x, *y = tup1 #first assigned to x rest assigned to y
print("X :",x, "Y:",y)


# In[ ]:


tup1= (10,20,50,100,45,234,13,53,13,4,5,2,2,34,5,3)
for x in tup1:
    print(x, end =' ')


# In[ ]:


tup1= (10,20,50,100,45,234,13)
indices = range(len(tup1))
for i in indices:
    print("tup1[{}]: ".format(i), tup1[i])


# In[ ]:


t1 = ( 1, 2, 3, 4, 5)
t2 = ('one', 'two', 'three')
t3 = t1 + t2
print(t3)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5)
t2 = ('one', 'two', 'three')
l1 = list(t1)
l2 = list(t2)
l1.extend(l2)
t1 = tuple(l1)
print(t1)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5)
t2 = ('one', 'two', 'three')
for t in t2:
    t1+=(t,)
print(t1)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5)
print(t1)
x = t1.index(4)
print("Index of number is ",x)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5, 1, 4,2,2,4,5,1,3,4,1,1,3,4,56,6)
c = t1.count(1)
print("Count of 1 is :", c)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5, 1, 4,2,2,4,5,1,3,4,1,1,3,4,56,6)
t2 = ()
for x in t1:
    if x not in t2:
        t2+=(x,)
print("Original :",t1)
print("unique :",t2)


# In[ ]:


t1 = ( 1, 2, 3, 4, 5, 1, 4,2,2,4,5,1,3,4,1,1,3,4,56,6)
total = 0
for x in t1:
    total += x
print("SUM :", total)

total = sum(t1)
print("sum :", total)


# In[ ]:


import random
t1 = ()
for i in range(5):
    x = random.randint(0,100)
    t1 += (x,)
print(t1)


# # Sets
# A set is one of the built-in data types in Python. In mathematics, set is a collection of distinct objects. Set data type is Python's implementation of a set. Objects in a set can be of any data type.
# 
# Set in Python also a collection data type such as list or tuple. However, it is not an ordered collection, i.e., items in a set or not accessible by its positional index. A set object is a collection of one or more immutable objects enclosed within curly brackets {}.
# Set is a collection of distinct objects. Even if you repeat an object in the collection, only one copy is retained in it.

# In[ ]:


s1 = {"a", "b", 2, 6}
s2 = {"Set can hold any value"}
print(s1)
print(s2)


# In[ ]:


l1 = ['a', 'b', 14, 657, 65 ]
s1 = set(l1)
t1 = (1, 7 ,85, 'abf')
s2 = set(t1)
string ="HELLooo!!!!!!!!"
s3 = set(string)
print(s1)
print(s2)
print(s3)


# In[ ]:


s1 = {1,6,4,4,1,8,22,88,84,321,12,8,8,9,1}
print(s1)


# In[ ]:


s1 = {"a", "b", 2, 6}
for x in s1:
    print(x)


# In[ ]:


alpha = {'a','b','c','d'}
alpha.add('e')
print(alpha)


# In[ ]:


s1 ={1,2,3,4,5,6,7}
s2 = {99,69,33,22,45,67,31}
s2.update(s1)
print(s2)


# In[ ]:


s1 = set('hello')
s1.update('world')
print(s1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




