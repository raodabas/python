import sqlite3

bag = sqlite3.connect("a.vt")
# tabloya bağlandık

cursor = bag.cursor()
# cursor isimli değişken veritabanı üzerinde
# işlem yapmak için kullanılan imleçtir

cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)") # Sorguyu çalıştırıyoruz.
bag.commit() # sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

bag.close() # bağlantı koparıldı.