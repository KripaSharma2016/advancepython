'''
Created on 05-Apr-2017

@author: ks016399
'''
'''
A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
'''
'''
A set is an unordered collection of elements.
The sets module provides classes for constructing and manipulating unordered collections of unique elements. 
Common uses include membership testing, removing duplicates from a sequence, 
and computing standard math operations on sets such as intersection, union, difference, and symmetric difference.

# initialization of set
set1 = {}
print(type(set1))
first_set = set()
print(type(first_set)) '''
#firstSet = {1,2,3,4,5,6}
#print(firstSet)

#set do not have duplicates
#secondSet = {1,1,1,1,1,1,2,2,2,3,3,3}
#print(secondSet)

#set cannot have mutable items
#thirdSet = {1,[2,3,4,5],2,3}
#print(thirdSet)
'''thirdSet = {1,(2,3,4,5),2,3}
print(thirdSet)

# we can make set from list
fourthSet = set([1,2,3,4,5,1,2,3])
print(fourthSet)

Sets are mutable. But since they are unordered, indexing have no meaning.

We cannot access or change an element of set using indexing or slicing. Set does not support it.

We can add single element using the add() method and multiple elements using the update() method. 
The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.
'''
# how to add element '''
a = {1,2,3,4}
a.add(5)
print(a)
a.add(2)
print(a)
a.update([1,2,6,7,4])
print(a)

name = "center"
print(name.center(2))
#how to delete the items from set
'''
A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.

The following example will illustrate this.'''

b = {1,2,3,4}
b.discard(6)
print(b)
b.remove(6)
print(b)

''''
>>> from sets import Set
>>> engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
>>> programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
>>> managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
>>> employees = engineers | programmers | managers           # union
>>> engineering_management = engineers & managers            # intersection
>>> fulltime_management = managers - engineers - programmers # difference
>>> engineers.add('Marvin')                                  # add element
>>> print engineers 
Set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
>>> employees.issuperset(engineers)     # superset test
False
>>> employees.update(engineers)         # update from another set
>>> employees.issuperset(engineers)
True
>>> for group in [engineers, programmers, managers, employees]: 
...     group.discard('Susan')          # unconditionally remove element
...     print group
...
Set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
Set(['Janice', 'Jack', 'Sam'])
Set(['Jane', 'Zack', 'Jack'])
Set(['Jack', 'Sam', 'Jane', 'Marvin', 'Janice', 'John', 'Zack'])
'''

'''
>>> x = {"a","b","c","d","e"}
>>> y = {"c","d"}
>>> x.issubset(y)
False
>>> y.issubset(x)
True
>>> x < y
False
>>> y < x # y is a proper subset of x
True
>>> x < x # a set can never be a proper subset of oneself.
False
>>> x <= x 
True
>>> 
'''    
'''
>>> x = {"a","b","c","d","e"}
>>> y = {"c","d"}
>>> x.issuperset(y)
True
>>> x > y
True
>>> x >= y
True
>>> x >= x
True
>>> x > x
False
>>> x.issuperset(x)
True
>>> 
'''


set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}
print(set_a ^ set_b)