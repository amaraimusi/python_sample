from thinc.layers import list2array
print ('インデックス付のループ | index付のfor文')

list = {'animal_name': '猫ちゃん', 'age': 3, 'place': '家の中'}

print(list['animal_name'])

for k, v in list.items():
    print(k, v)
 
print('-----------')   

for v in list.values():
    print(v)

print('-----------')

for v in list:
    print(v)

print('-----------')    

for k in list.keys():
    print(k)

print('-----------')    

for i, v in enumerate(list):
    print(i)
    print(v)

print('-----------')   

list2 = ['やぎ','ぶた','うし']
for v in list2:
    print(v)
