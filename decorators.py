'''
Created on 17-May-2017

@author: ks016399
'''
'''def my_function(num):
    return num+1

my_var = my_function
print(my_var(10))
print(my_function(12))

def function_one(func):
    print("this is my function one!")
    func()
def function_two():
    print("this is my function two")
function_one(function_two)

# Function returning function

def f1():
    print("this is my function f1")
    def f2():
        print("this is funtion f2")
    return f2()
my_var = f1
my_var()'''
'''def f1():
    print("this is my function f1")
    def f2():
        print("this is funtion f2")
    return f2
my_var = f1()
my_var()

# decorators in function
def my_decorator(printer):
    def my_printer(*args,**kwargs):
        print("i am in inside my_printer method {}".format(printer.__name__))
        return printer(*args,**kwargs)
    return my_printer

@my_decorator
def show():
    print("this is show function!")

#my_var = my_decorator(show)
#my_var()
show()

@my_decorator
def show_with_params(my_number,my_string):
    print("these are the passed values are ->>> {} and {}".format(my_number,my_string))

show_with_params(100,"hello")

# Decorators as classes and methods
# decorators in function
def my_decorator(printer):
    def my_printer(*args,**kwargs):
        print("i am in inside my_printer method {}".format(printer.__name__))
        return printer(*args,**kwargs)
    return my_printer
'''
class MyDecorator():
    def __init__(self,printer):
        self.printer=printer
        
    def __call__(self,*args,**kwargs):
        print("this is call method of MyDecorator class!")
        return self.printer(*args,**kwargs)
    
    #def user_defined_decorator(self,*args,**kwargs):
    #   print("this is user defined decorator!")
    #    return self.printer(*args,**kwargs)

@MyDecorator
def show_with_params(my_number,my_string):
    print("these are the passed values are ->>> {} and {}".format(my_number,my_string))

show_with_params(100,"hello")    