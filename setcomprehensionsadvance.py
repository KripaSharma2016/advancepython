'''
Created on 13-May-2017

@author: ks016399
'''
set_A = {1,2,3}
set_B = {5,6,7}
result_set = set()
for i in set_A:
    for j in set_A:
        result_set.add((i,j))
print(result_set)     

print({(x,y) for x in set_A for y in set_B})  
print({x*y for x in set_A for y in set_B})  

#dictionary 

dict_one = {'ramesh':120,'suresh':200,'rahul':300}
dict_two = {'rohan':800,'riya':900}
#merged_dict = dict_one + dict_two
merged_dict = {}
for d in (dict_one,dict_two):
    for k,v in d.items():
        merged_dict[k]=v
merged_dict = {k: v for d in (dict_one, dict_two) for k, v in d.items()}    
print(merged_dict)

  


        