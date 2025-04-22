# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:47:19 2025

@author: Administrator
"""

import pandas as pd
import sqlite3
import logging

# Loglama yapılandırması
logging.basicConfig(
    filename='veritabani_islemleri.log',  # Loglar bu dosyaya yazılacak
    level=logging.INFO,  # INFO seviyesindeki logları kaydedecek
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Loglama: İşleme başlama
logging.info("Veri işleme başlatıldı.")

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('ilk_veritabanim.db')

# Basit bir veri listesi oluşturalım
veriler = {'isim': ['Ahmet', 'Ayşe', 'Mehmet'], 
           'yas': [25, 30, 28]}

# Listeden Pandas DataFrame oluşturalım
df = pd.DataFrame(veriler)
logging.info("Pandas DataFrame başarıyla oluşturuldu.")

# Veri kalitesi kontrolü
if df.isnull().values.any():
    logging.warning("Eksik veri tespit edildi!")
else:
    logging.info("Eksik veri bulunamadı.")

# Yaş ortalamasını hesaplayıp yazdıralım
ortalama_yas = df['yas'].mean()
logging.info(f"Yaş ortalaması hesaplandı: {ortalama_yas}")

# DataFrame'i SQLite veritabanına kaydedelim
df.to_sql('kisiler', conn, if_exists='replace', index=False)
logging.info("Veri SQLite veritabanına başarıyla kaydedildi.")

# Veritabanındaki verileri kontrol edelim
logging.info("Veritabanındaki veriler çekiliyor...")
sonuc = pd.read_sql_query("SELECT * FROM kisiler", conn)
logging.info(f"Veritabanından okunan veriler:\n{sonuc}")

# Bağlantıyı kapatalım
conn.close()
logging.info("SQLite veritabanı bağlantısı kapatıldı.")