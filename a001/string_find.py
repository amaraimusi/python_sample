print ('Pythonの覚書：文字列を検索して取得')



# 文字列を左側から印文字を検索し、左側の文字を切り出す
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から左側の文字列
def stringLeft(s, mark):
    a =s.find(mark)
    res = s[0:a]
    return res


# 文字列を左側から印文字を検索し、右側の文字を切り出す。
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から右側の文字列
def stringRight(s, mark):
    a =s.find(mark)
    res = s[a+len(mark):]
    return res

# 文字列を右側から印文字を検索し、左側の文字を切り出す
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から左側の文字列
def stringLeftRev(s, mark):
    a =s.rfind(mark)
    res = s[0:a]
    return res


# 文字列を右側から印文字を検索し、右側の文字を切り出す
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から右側の文字列
def stringRightRev(s, mark):
    a =s.rfind(mark)
    res = s[a+len(mark):]
    return res





print('-----------')

print('#1 stringLeft:文字列を左側から印文字を検索し、左側の文字を切り出す')
str= 'ブタ:ネコ:ライオン:シカ'
res = stringLeft(str, ':')
print(str)
print(res)


print('-----------')

print('#2 stringRight:文字列を左側から印文字を検索し、右側の文字を切り出す。')
str= 'ブタ:ネコ:ライオン:シカ'
res = stringRight(str, ':')
print(str)
print(res)

print('-----------')

print('#3 stringLeftRev:文字列を右側から印文字を検索し、左側の文字を切り出す')
str= 'ブタ:ネコ:ライオン:シカ'
res = stringLeftRev(str, ':')
print(str)
print(res)

print('-----------')

print('#4 stringRightRev:文字列を右側から印文字を検索し、右側の文字を切り出す')
str= 'ブタ:ネコ:ライオン:シカ'
res = stringRightRev(str, ':')
print(str)
print(res)

print('-----------')
