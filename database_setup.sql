CREATE DATABASE ETicaretDB;
GO
USE ETicaretDB;
GO

-- 1. TABLOLAR
CREATE TABLE Kategoriler (
	KategoriID INT PRIMARY KEY IDENTITY(1,1),
	KategoriAdi NVARCHAR(50) NOT NULL
);

CREATE TABLE Musteriler (
	MusteriID INT PRIMARY KEY IDENTITY(1,1),
	Ad NVARCHAR(50) NOT NULL,
	Soyad NVARCHAR(50) NOT NULL,
	Sehir NVARCHAR(50) NULL,
	KayitTarihi DATETIME DEFAULT GETDATE()
);

CREATE TABLE Urunler (
	UrunID INT PRIMARY KEY IDENTITY(1,1),
	UrunAdi NVARCHAR(100) NOT NULL,
	Fiyat DECIMAL(18,2) NOT NULL,
	Stok INT DEFAULT 0,
	KategoriID INT,
	CONSTRAINT FK_Urunler_Kategoriler FOREIGN KEY (KategoriID) REFERENCES Kategoriler(KategoriID)
);

CREATE TABLE Siparisler (
    SiparisID INT PRIMARY KEY IDENTITY(1,1),
    MusteriID INT NOT NULL,
    SiparisTarihi DATETIME DEFAULT GETDATE(),
    CONSTRAINT FK_Siparisler_Musteriler FOREIGN KEY (MusteriID) REFERENCES Musteriler(MusteriID)
);

CREATE TABLE SiparisDetay (
    DetayID INT PRIMARY KEY IDENTITY(1,1),
    SiparisID INT NOT NULL,
    UrunID INT NOT NULL,
    Adet INT DEFAULT 1,
    SatisFiyati DECIMAL(18, 2) NOT NULL,
    CONSTRAINT FK_Detay_Siparisler FOREIGN KEY (SiparisID) REFERENCES Siparisler(SiparisID),
    CONSTRAINT FK_Detay_Urunler FOREIGN KEY (UrunID) REFERENCES Urunler(UrunID)
);
GO

-- 2. VIEW OLUŞTURMA
CREATE VIEW vw_SatisRaporu AS
SELECT
    S.SiparisID, M.Ad + ' ' + M.Soyad AS Musteri, M.Sehir,
    K.KategoriAdi, U.UrunAdi, SD.Adet, SD.SatisFiyati,
    (SD.Adet * SD.SatisFiyati) AS ToplamTutar, S.SiparisTarihi
FROM Siparisler S
INNER JOIN Musteriler M ON S.MusteriID = M.MusteriID
INNER JOIN SiparisDetay SD ON S.SiparisID = SD.SiparisID
INNER JOIN Urunler U ON SD.UrunID = U.UrunID
INNER JOIN Kategoriler K ON U.KategoriID = K.KategoriID;
GO

-- 3. STORED PROCEDURE
CREATE PROCEDURE sp_SiparisVer
    @MusteriID INT, @UrunID INT, @Adet INT
AS
BEGIN
    DECLARE @GuncelFiyat DECIMAL(18,2);
    DECLARE @MevcutStok INT;
    SELECT @GuncelFiyat = Fiyat, @MevcutStok = Stok FROM Urunler WHERE UrunID = @UrunID;

    IF @MevcutStok >= @Adet
    BEGIN
        INSERT INTO Siparisler (MusteriID, SiparisTarihi) VALUES (@MusteriID, GETDATE());
        DECLARE @YeniSiparisID INT = SCOPE_IDENTITY();
        INSERT INTO SiparisDetay (SiparisID, UrunID, Adet, SatisFiyati)
        VALUES (@YeniSiparisID, @UrunID, @Adet, @GuncelFiyat);
        UPDATE Urunler SET Stok = Stok - @Adet WHERE UrunID = @UrunID;
    END
    ELSE
    BEGIN
        THROW 51000, 'Yetersiz Stok! Sipariş oluşturulmadı.', 1;
    END
END;
GO