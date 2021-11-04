print ('テキストファイルを読み込む')

f = open('./sample/sample1.txt', 'r', encoding='UTF-8')

data = f.read()
print(data)

f.close()
