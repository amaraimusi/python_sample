print ('PythonでSQLite3を扱う')

import sqlite3

dao = sqlite3.connect(
    "test5.sqlite3", #データベースのファイル名
    isolation_level=None, #Noneは自動コミットを表す
)

sql = """
    CREATE TABLE nekos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        neko_name VARCHAR(50),
        neko_age INTEGER
    );
"""
# dao.execute(sql)     #sql文を実行

dao.execute("INSERT INTO nekos(neko_name, neko_age) VALUES ('イッパイアッテナ', 12);")  

# SELECT文の実行とデータ取得
res = dao.execute("SELECT * FROM nekos;")  
#data = res.fetchone() # 1行だけ取得
data = res.fetchall() # すべて取得

print(data)

dao.close()