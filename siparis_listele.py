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

        print("\n" + "=" * 70)
        print(f"{'SİPARİŞ GEÇMİŞİ VE CİRO RAPORU':^70}")
        print("=" * 70)

        cursor.execute("SELECT * FROM vw_SatisRaporu ORDER BY SiparisTarihi DESC")

        print(f"{'Sipariş No':<12} | {'Tarih':<20} | {'Müşteri':<15} | {'Ürün':<15} | {'Tutar':>8}")
        print("-" * 75)

        genel_toplam = 0
        kayit_sayisi = 0

        for row in cursor:
            siparis_id = row[0]
            musteri = row[1][:15]
            urun = row[4][:15]
            tutar = row[7]
            tarih = str(row[8])[:19]

            print(f"{siparis_id:<12} | {tarih:<20} | {musteri:<15} | {urun:<15} | {tutar:>8.2f} TL")

            genel_toplam += tutar
            kayit_sayisi += 1

        print("-" * 75)
        print(f"TOPLAM KAYIT: {kayit_sayisi}")
        print(f"GENEL CİRO  : {genel_toplam:,.2f} TL")
        print("=" * 70 + "\n")

except Exception as e:
    print(f"HATA: {e}")