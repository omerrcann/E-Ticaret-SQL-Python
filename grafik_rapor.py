import pyodbc
import matplotlib.pyplot as plt

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

        sorgu = """
                SELECT KategoriAdi, SUM(ToplamTutar) as Ciro
                FROM vw_SatisRaporu
                GROUP BY KategoriAdi
                ORDER BY Ciro DESC \
                """
        cursor.execute(sorgu)


        kategoriler = []
        cirolar = []

        for row in cursor:
            kategoriler.append(row[0])
            cirolar.append(row[1])

        print("Veriler çekildi, grafik hazırlanıyor...")


        plt.figure(figsize=(10, 6))  # Pencere boyutu
        plt.bar(kategoriler, cirolar, color='skyblue')
        plt.title('Kategori Bazlı Ciro Analizi', fontsize=16)
        plt.xlabel('Kategoriler', fontsize=12)
        plt.ylabel('Toplam Ciro (TL)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Arkaya çizgi at


        for i, ciro in enumerate(cirolar):
            plt.text(i, ciro + 100, f"{ciro:.0f} TL", ha='center', va='bottom')

        plt.show()

except Exception as e:
    print(f"HATA: {e}")