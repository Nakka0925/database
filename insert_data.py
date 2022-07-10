import sqlite3

name = input('名前は？: ')
gakunen = input('学年は？： ')
touroku = input('選手登録は？： ')
state = input('活動状態は？： ')

dict = {"県登録" : 2000, "学連登録" : 7250, "学連登録＆県登録" : 9250, "無" : 0, "休部" : 0, "活動中" : 4000}

con = sqlite3.connect('TEST.db')
cur = con.cursor()
sql = 'INSERT INTO ("名前", "学年", "登録関係", "登録料金(円)", "状態", "部費(円)") sample values (?,?,?,?,?,?)'
data = [name, gakunen, touroku, dict[touroku], state, dict[state]]
cur.execute(sql, data)

cur.close()
con.commit()
con.close()