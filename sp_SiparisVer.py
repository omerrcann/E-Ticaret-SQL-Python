import pyodbc

server = r'Omer\SQLEXPRESS'
database = 'ETicaretDB'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()

        print("--- 🛒 SİPARİŞ SİSTEMİ ---")
        musteri_id = input("Müşteri ID (Örn: 1): ")
        urun_id = input("Ürün ID (1-Laptop, 2-Mouse, 3-Kot, 4-SQL Kitap): ")
        adet = input("Kaç Adet?: ")


        sql_komutu = "EXEC sp_SiparisVer @MusteriID=?, @UrunID=?, @Adet=?"
        parametreler = (musteri_id, urun_id, adet)

        print("\nİşlem gönderiliyor...")
        cursor.execute(sql_komutu, parametreler)

        conn.commit()

        print("✅ Sipariş Başarıyla Oluşturuldu!")
        print("Veritabanındaki Stok otomatik olarak düşüldü.")

except pyodbc.Error as ex:
    print(f"❌ SQL HATASI: {ex}")
except Exception as e:
    print(f"❌ HATA: {e}")
    cursor.execute("SELECT UrunAdi, Stok FROM Urunler WHERE UrunID = 2")
    row = cursor.fetchone()
    print(f"\n🔍 GÜNCEL STOK KONTROLÜ:")
    print(f"Ürün: {row[0]} | Kalan Stok: {row[1]}")