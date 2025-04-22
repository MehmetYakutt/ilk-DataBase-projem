# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:48:36 2025

@author: Administrator
"""

import pandas as pd
import sqlite3

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('ilk_veritabanim.db')

# Basit bir veri listesi oluşturalım
veriler = {'isim': ['Ahmet', 'Ayşe', 'Mehmet'], 
           'yas': [25, 30, 28]}

# Listeden Pandas DataFrame oluşturalım
df = pd.DataFrame(veriler)

# DataFrame'i ekrana yazdıralım
print("Merhaba Veri Dünyası!")
print(df)

# Yaş ortalamasını hesaplayıp yazdıralım
ortalama_yas = df['yas'].mean()
print(f"Yaş Ortalaması: {ortalama_yas}")

# DataFrame'i SQLite veritabanına kaydedelim
df.to_sql('kisiler', conn, if_exists='replace', index=False)

# Veritabanındaki verileri kontrol edelim
print("\nVeritabanından okunan veriler:")
sonuc = pd.read_sql_query("SELECT * FROM kisiler", conn)
print(sonuc)

# Bağlantıyı kapatalım
conn.close()
