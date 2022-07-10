import sqlite3
import pandas as pd


"""
    ・df = pd.read_csv("kadai2.csv")
    ・df.to_sql('sample', conn, if_exists = "replace", index = None)
    
    csvから読み取るとき以外不要
"""


# pandasでカレントディレクトリにあるcsvファイルを読み込む
#df = pd.read_csv("kadai2.csv")

dbname = 'TEST.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
#df.to_sql('sample', conn, if_exists = "replace", index = None)

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM sample'

sum = 0

for row in cur.execute(select_sql):
    print(row[0], "\t", "個人徴収金額：" + str(row[3] + row[5]))
    sum += row[3] + row[5]

print("合計徴収金額：" + str(sum))

cur.close()
conn.close()