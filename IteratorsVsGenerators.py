'''
Created on 13-May-2017

@author: ks016399
'''
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    
my_iter = iter(my_list)
print(my_iter.next())
print(my_iter.next())
print(my_iter.next())
print(my_iter.next())
print(my_iter.next())


class MyItrableClass:
    def __init__(self):
        pass
    def __iter__(self):
        self.num  =0
        return self
    def __next__(self):
        num = self.num
        self.num +=1
        return num
itr = iter(MyItrableClass())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__iter__())
print(itr.__next__())


''' generators.....................................'''
def my_gen():
    a,b,c,d = 12,3,4,100
    yield a
    yield b
    yield c
    yield d
print(my_gen())
it1 = my_gen()
try:
    print(it1.next())
    print(it1.next())
    print(it1.next())
    print(it1.next())
    print(it1.next())
except StopIteration as ex:
    print("Iteration got stopped!")




