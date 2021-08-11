
import os

cur_dp = os.getcwd()
print (cur_dp)

list = {'animal_name': '赤犬', 'age': 2, 'place': '家の外'}

print(list['animal_name'])

for k, v in list.items():
    print(k, v)
    

for v in list.values():
    print(v)
    
for k in list.keys():
    print(k)