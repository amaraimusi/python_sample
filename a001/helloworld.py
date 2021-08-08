print ('HelloWorld2')

list = {'animal_name': '猫ちゃん', 'age': 3, 'place': '家の中'}

print(list['animal_name'])

for k, v in list.items():
    print(k, v)
    

for v in list.values():
    print(v)
    
for k in list.keys():
    print(k)