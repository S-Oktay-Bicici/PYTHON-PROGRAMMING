import sqlite3

db = sqlite3.connect("kitaplar.db")
imlec = db.cursor()

imlec.execute("SELECT * FROM 'kitaplık tablosu' WHERE yazar = 'Paulo Coelho'")

veriler = imlec.fetchall()

for i in veriler:
    print(i)



db.close()