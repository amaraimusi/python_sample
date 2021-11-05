import datetime

print ('Pythonの覚書：現在日時を取得 | datetime')

dt = datetime.datetime.now()
u = dt.strftime("%Y%m%d%H%M%S")
print(type(dt))
print(dt)
print(u)



