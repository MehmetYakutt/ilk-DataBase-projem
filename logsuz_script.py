# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:48:36 2025

@author: Administrator
"""
import pandas as pd
import sqlite3
import logging

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# SQLite veritabanı bağlantısı oluştur
try:
    conn = sqlite3.connect('ilk_veritabanim.db')
    logging.info("Veritabanı bağlantısı başarıyla oluşturuldu")
except Exception as e:
    logging.error(f"Veritabanı bağlantısı oluşturulamadı: {str(e)}")
    exit(1)

# Basit bir veri listesi oluşturalım
veriler = {'isim': ['Ahmet', 'Ayşe', 'Mehmet'], 
           'yas': [25, 30, 28]}

# Listeden Pandas DataFrame oluşturalım
df = pd.DataFrame(veriler)
logging.info("DataFrame oluşturuldu")

# DataFrame'i ekrana yazdıralım
print("Merhaba Veri Dünyası!")
print(df)

# Yaş ortalamasını hesaplayıp yazdıralım
ortalama_yas = df['yas'].mean()
print(f"Yaş Ortalaması: {ortalama_yas}")
logging.info(f"Yaş ortalaması hesaplandı: {ortalama_yas}")

# DataFrame'i SQLite veritabanına kaydedelim
try:
    df.to_sql('kisiler', conn, if_exists='replace', index=False)
    logging.info("Veriler 'kisiler' tablosuna başarıyla kaydedildi")
except Exception as e:
    logging.error(f"Verileri veritabanına kaydetme hatası: {str(e)}")

# Veritabanındaki verileri kontrol edelim
try:
    print("\nVeritabanından okunan veriler:")
    sonuc = pd.read_sql_query("SELECT * FROM kisiler", conn)
    print(sonuc)
    logging.info(f"Veritabanından {len(sonuc)} satır veri okundu")
except Exception as e:
    logging.error(f"Veritabanından veri okuma hatası: {str(e)}")

# Bağlantıyı kapatalım
conn.close()
logging.info("Veritabanı bağlantısı kapatıldı")
