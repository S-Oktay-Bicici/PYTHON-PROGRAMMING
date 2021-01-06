import sqlite3

db = sqlite3.connect("kitaplar.db")
imlec = db.cursor()

imlec.execute("SELECT * FROM 'kitaplık tablosu'")

veriler = imlec.fetchmany(4)

for i in veriler:
    print(i)



db.close()