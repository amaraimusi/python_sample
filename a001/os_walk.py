
import os

cur_dp = os.getcwd()
print (cur_dp)


# sampleディレクトリの全階層にあるサブディレクトリとファイルの名前をすべて取得する
for curDir, dirs, files in os.walk('./sample'):
    print('---')
    print(curDir)
    print(dirs)
    print(files)
