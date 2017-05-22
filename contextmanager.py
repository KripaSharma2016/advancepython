'''
Created on 19-May-2017

@author: ks016399
'''

my_fp = open('myfile.txt','w')
try:
    my_fp.write("hello india!")
finally:
    my_fp.close()

with open("myfile.txt",'a') as fp:
    fp.write("hello")
    
    
class MyContextManager(object):
    def __init__(self,file_name,mode):
        self.fp = open(file_name,mode)
    def __enter__(self):
        return self.fp
    def __exit__(self,type,value,tracback):
        self.fp.close()

with MyContextManager('mynewfile.txt','w') as fp:
    fp.write("this is my newfile!")
    

'''

    The with statement stores the __exit__ method of File class.
    It calls the __enter__ method of File class.
    __enter__ method opens the file and returns it.
    the opened file handle is passed to opened_file.
    we write to the file using .write()
    with statement calls the stored __exit__ method.
    the __exit__ method closes the file.
'''