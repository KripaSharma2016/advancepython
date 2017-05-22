'''
Created on 13-May-2017

@author: ks016399
'''
my_f_set = frozenset([1,2,3,4])
print(my_f_set)
#my_f_set.add(78)
#print(my_f_set)
my_list = [1,2,3,4]
print(frozenset(my_list))
#my_f_set = frozenset([1,2,3,[1,2,3],4,5,6])
#print(my_f_set)
my_dict = {'product':'apple','cost':'120'}
print(frozenset(my_dict))

f_set_parking_allot = frozenset(['A_1','A_2','A_3'])
cars = ['bmw-x2','honda','maruti']
my_list = zip(f_set_parking_allot,cars)
#alloted_space = {x:y for x,y in f_set_parking_allot,cars}
print(my_list)

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
def get_prime():
    results = []
    gen_prime = gen_primes()
    for i in range(100):
        results.append(gen_prime.next())
    return results
my_f_prime_set = frozenset(get_prime())
print(my_f_prime_set)   
num  = input("enter any number to check weather it is prime of not:")
if num in my_f_prime_set:
    print("yess! it is prime number!")
else:
    print("Not a prime number!")    
        
    






