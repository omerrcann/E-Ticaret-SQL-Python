# 🛒 SQL & Python E-Ticaret Yönetim Sistemi

Bu proje, **SQL Server** veritabanı ile **Python** programlama dilini entegre eden, transaction güvenliğine sahip bir E-Ticaret yönetim sistemidir.

Proje; ilişkisel veritabanı tasarımı, saklı yordamlar (Stored Procedures), tetikleyiciler (Triggers) ve veri görselleştirme tekniklerini içermektedir.

## 🚀 Özellikler

- **İlişkisel Veritabanı:** Kategoriler, Ürünler, Müşteriler, Siparişler ve Detaylar arasındaki 1-to-Many ve Many-to-Many ilişkiler.
- **İşlem Güvenliği (ACID):** `sp_SiparisVer` prosedürü ile stok kontrolü ve sipariş oluşturma işlemleri atomik olarak yönetilir.
- **Otomatik Stok Yönetimi:** Sipariş iptallerinde stoğu otomatik güncelleyen **Trigger** yapısı.
- **Dinamik Raporlama:** SQL Views kullanılarak oluşturulan satış raporları.
- **Veri Görselleştirme:** Python `matplotlib` kütüphanesi ile kategori bazlı ciro grafikleri.

## 🛠️ Kullanılan Teknolojiler

- **Veritabanı:** MS SQL Server (T-SQL)
- **Dil:** Python 3.x
- **Kütüphaneler:** `pyodbc`, `matplotlib`
- **IDE:** PyCharm, SSMS

## 📂 Proje Yapısı

- `database_setup.sql` ➔ Veritabanı tabloları, View, SP ve Trigger'ların kurulum kodları.
- `sp_SiparisVer.py` ➔ Sipariş girişi yapan ve stok kontrolü sağlayan modül.
- `siparis_listele.py` ➔ Geçmiş siparişleri ve toplam ciroyu listeleyen raporlama aracı.
- `grafik_rapor.py` ➔ Satış verilerini analiz edip grafik çizen araç.

## ⚙️ Kurulum

1. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
