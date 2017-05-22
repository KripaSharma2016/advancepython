'''
Created on 20-May-2017

@author: ks016399
'''

        

class MySingleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    

if __name__ == '__main__':
    obj1 = MySingleton()
    obj2 = MySingleton()
    print(id(obj1))
    print(id(obj2))
        
        
        
        