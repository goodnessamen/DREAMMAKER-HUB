#!/usr/bin/env python
# coding: utf-8

# # PYTHON PROGRAMMING SELF TUTORIAL

# In[7]:


first = 'Amenze'


# In[8]:


print (first)


# In[2]:


last = 'Chidobi'


# In[ ]:





# In[9]:


print (last)


# In[22]:


message = first + ' [' + last + '] is a coder


# In[23]:


msg = f'{first} [{last}] is a coder


# In[1]:


print("Hello, World!") #This is a comment


# In[2]:


#print("Hello, World!")
print("Cheers, Mate!")


# In[25]:


Course = 'Python for Beginners'


# In[26]:


print(Course)   ## print function


# In[27]:


print(len(Course))   ##len function


# In[29]:


Course = 'Python for Beginners'


# In[30]:


print(Course)


# In[31]:


print(Course.upper())


# In[32]:


print(Course.lower())


# In[33]:


print(Course.find('P'))


# In[35]:


print(Course.find('o'))


# In[ ]:


replace("Beginners", "Absolute Beginners")


# ## Change List Items

# In[ ]:


#
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":


# In[36]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# ## Change a Range of Item Values

# In[ ]:


## Change the second value by replacing it with two new values:


# In[37]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[ ]:


##Insert "watermelon" as the third item:


# In[39]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# ##  Append Items

# In[ ]:


## To add an item to the end of the list, use the append() method:


# In[41]:


thislist = ["apple", "banana", "cherry"]  ##Using the append() method to append an item:
thislist.append("orange")
print(thislist)


# In[44]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange"), ("strawberry")
print(thislist)


# ## Insert Items

# In[ ]:


## The insert() method inserts an item at the specified index:


# In[3]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[ ]:


##Note: As a result of the examples above, the lists will now contain 4 items.


# ### Extend List

# In[ ]:


##To append elements from another list to the current list, use the extend() method.

Example
Add the elements of tropical to thislist:


# In[2]:


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# In[ ]:


##The elements will be added to the end of the list.


# ### Add Any Iterable

# In[ ]:


## The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:


# In[4]:


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# ## Python Collections (Arrays)

# In[ ]:


## There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.


# ### Python - Remove List Items

# In[ ]:


## Remove Specified Item
## The remove() method removes the specified item.
Example
Remove "banana":


# In[5]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[ ]:


## Remove Specified Index
## The pop() method removes the specified index.
Example
Remove the second item:


# In[6]:


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[ ]:


## If you do not specify the index, the pop() method removes the last item.
Example
Remove the last item:


# In[7]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# In[ ]:


## The del keyword also removes the specified index:
Example
Remove the first item:


# In[10]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[12]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[ ]:


## The del keyword can also delete the list completely.
Example
Delete the entire list:


# In[14]:


thislist = ["apple", "banana", "cherry"]
del thislist


# ### Clear the List
# 

# In[ ]:


The clear() method empties the list.
The list still remains, but it has no content.
Example
Clear the list content:


# In[15]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# ### Python - Loop Lists

# In[ ]:


Loop Through a List
You can loop through the list items by using a for loop:

Example
Print all items in the list, one by one:


Learn more about for loops in our Python For Loops Chapter.


# In[27]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# ## Loop Through the Index Numbers

# In[ ]:





# In[ ]:


You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:


# In[16]:


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# In[ ]:


##  The iterable created in the example above is [0, 1, 2].


# ### Using a While Loop

# In[ ]:


You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
Learn more about while loops in our Python While Loops Chapter.

Example
Print all items, using a while loop to go through all the index numbers


# In[28]:


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# ### Looping Using List Comprehension

# In[ ]:


List Comprehension offers the shortest syntax for looping through lists:

Example
A short hand for loop that will print all items in a list:
Learn more about list comprehension in the next chapter: List Comprehension.


# In[29]:


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# ## Sort Descending
# To sort descending, use the keyword argument reverse = True:
# 
# Example
# Sort the list descending:
# 
# 

# In[18]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[19]:


## Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# In[20]:


##  Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# In[ ]:


## Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# ### Python - Sort Lists
# ### Sort List Alphanumerically

# In[ ]:



List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Example
### Sort the list alphabetically:





Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

Example
Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Example
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
Reverse Order
get_ipython().set_next_input('What if you want to reverse the order of a list, regardless of the alphabet');get_ipython().run_line_magic('pinfo', 'alphabet')

The reverse() method reverses the current sorting order of the elements.

Example
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# In[31]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Example
# ### Sort the list numerically:

# In[32]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# ### Sort Descending
# To sort descending, use the keyword argument reverse = True:
# 
# Example
# Sort the list descending:

# In[33]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[ ]:


Example
Sort the list descending:


# In[35]:


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# ## Python - Copy Lists
# ### Copy a List

# In[ ]:


You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
Example
Make a copy of a list with the copy() method:


# In[37]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# ### Another way to make a copy is to use the built-in method list().
# Example
# Make a copy of a list with the list() method:

# In[38]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[ ]:


Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Example
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
Or you can use the extend() method, which purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# ### Python Lists

# In[ ]:


mylist = ["apple", "banana", "cherry"]
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

Example
Create a List:


# In[2]:


thislist = ["apple", "banana", "cherry"]
print(thislist)


# ### Python - Access List Items

# In[ ]:


Access Items
List items are indexed and you can access them by referring to the index number:

Example
Print the second item of the list:


# In[3]:


thislist = ["apple", "banana", "cherry"]
print(thislist[1])
### Note: The first item has index 0.


# ### Negative Indexing

# In[ ]:


Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:


# In[4]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# ### Range of Indexes

# In[ ]:


You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:


# In[5]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
### Note: The search will start at index 2 (included) and end at index 5 (not included).


# In[ ]:


Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:

Example
This example returns the items from the beginning to, but NOT including, "kiwi":


# In[6]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# In[ ]:


By leaving out the end value, the range will go on to the end of the list:

Example
This example returns the items from "cherry" to the end:


# In[7]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# ### Range of Negative Indexes

# In[ ]:


Specify negative indexes if you want to start the search from the end of the list:

Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):


# In[8]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# ### Check if Item Exists

# In[ ]:


To determine if a specified item is present in a list use the in keyword:
Example
Check if "apple" is present in the list:


# In[9]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# ### List Items

# In[ ]:


List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

Example
Lists allow duplicate values:


# In[1]:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# In[ ]:


Change Item Value
To change the value of a specific item, refer to the index number:

Example
Change the second item:


# In[10]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# ### Change a Range of Item Values

# In[ ]:


To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values:

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":


# In[12]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[ ]:


Note: The length of the list will change when the number of items inserted does not match the number of items replaced.


# In[14]:


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# In[ ]:


If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:


# In[15]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# ### Insert Items

# In[ ]:


To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:


Note: As a result of the example above, the list will now contain 4 items.


# In[16]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# ### Python - Add List Items
# ### Append Items

# In[ ]:


To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:


# In[17]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# ### Insert Items

# In[ ]:


To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert an item as the second position:
### Note: As a result of the examples above, the lists will now contain 4 items.


# In[18]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# ### Extend List

# In[ ]:





# In[ ]:


To append elements from another list to the current list, use the extend() method.

Example
Add the elements of tropical to thislist:

## The elements will be added to the end of the list.


# In[19]:


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# ### Add Any Iterable

# In[ ]:


The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:


# In[20]:


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# ### Python - Remove List Items

# ### Remove

# In[ ]:


Remove Specified Item
The remove() method removes the specified item.

Example
Remove "banana":


# In[21]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# ### Remove Specified Index

# ### Pop

# In[ ]:


The pop() method removes the specified index.

Example
Remove the second item:


# In[22]:


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[ ]:


If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:


# In[23]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# ### Del

# In[ ]:


The del keyword also removes the specified index:

Example
Remove the first item:


# In[24]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[ ]:


The del keyword can also delete the list completely.

Example
Delete the entire list:


# In[25]:


thislist = ["apple", "banana", "cherry"]
del thislist


# In[ ]:


Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:


# In[26]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# ### Python Tuples

# ### Join Two Lists

# In[ ]:


## There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Example
Join two list:


# In[24]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[26]:


list3 = list1 + list2
print(list3)


# In[ ]:


## Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:


# In[27]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[29]:


for x in list2:
    list1.append(x)
    
print(list1)


# In[ ]:


## Or you can use the extend() method, which purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:


# In[30]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# ### Python - List Methods

# In[ ]:


## List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


# ### NUMPY NUMERICAL PYTHON

# In[ ]:


NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".


# In[4]:


import numpy as np
print(np.__version__)


# ### Checking NumPy Version

# In[2]:


import numpy as np

print(np.__version__)


# In[ ]:


Import NumPy
Once NumPy is installed, import it in your applications by adding the import keyword:

import numpy
Now NumPy is imported and ready to use.

Example


# In[ ]:


### NumPy Creating Arrays


# In[5]:


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


# In[ ]:



type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

Example
Use a tuple to create a NumPy array:


# In[6]:


import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)


# In[9]:


import numpy as np
arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))


# In[ ]:


### Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.


# ### 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# Example
# Create a 0-D array with value 42

# In[11]:


import numpy as np
arr = np.array(42)
print(arr)
print(type(arr))


# ### 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# 
# These are the most common and basic arrays.
# 
# Example
# Create a 1-D array containing the values 1,2,3,4,5:

# In[12]:


import numpy as np
arr = np.array([1,2,3,4,5,])
print(arr)


# ### 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# 
# These are often used to represent matrix or 2nd order tensors.
# 
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
# 
# Example
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
# 

# In[13]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr)
print(type(arr))


# ### 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# 
# These are often used to represent a 3rd order tensor.
# 
# Example
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

# In[14]:


import numpy as np
arr = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr)
print(type(arr))


# In[ ]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
get_ipython().set_next_input('Check Number of Dimensions');get_ipython().run_line_magic('pinfo', 'Dimensions')
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Example
Check how many dimensions the arrays have:


# In[ ]:


import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


# In[ ]:






print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

Example
Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

Test Yourself With Exercises
Exercise:
Insert the correct method for creating a NumPy array.

arr = np.
([1, 2, 3, 4, 5])

