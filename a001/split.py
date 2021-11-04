print ('split 文字列分割のテスト')

str1 = 'neko inu   yagi\nSika\tTanuki';
list = str1.split()

print(list)

str2 = '猫 , 犬,ヤギ,シカ,    タヌキ   X';
list = str2.split(',')

print(list)
