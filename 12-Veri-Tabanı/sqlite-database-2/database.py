import sqlite3 

veriler = [
    ("Ahmet Ümit","İstanbul Hatırası"),
    ("Yaşar Kemal","İnce Memed"),
    ("Paulo Coelho","Simyacı"),
    ("Paulo Coelho","Aldatmak")]

db = sqlite3.connect("kitaplar.db")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'kitaplık tablosu' (yazar,kitap)")

for veri in veriler:
    imlec.execute("INSERT INTO 'kitaplık tablosu' VALUES (?,?)",veri)

db.commit()
db.close()
