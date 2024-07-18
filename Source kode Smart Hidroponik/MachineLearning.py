"""............................................................................................................."""
""" Kode by MERA X """


"""============================ LIBRARY ===================================="""
import pandas as pd # Digunakan untuk memanggil library pandas (pandas untuk mengolah tabel data)
from pymongo import MongoClient #Digunakan untuk memanggil library Mongo
from sklearn.preprocessing import LabelEncoder #digunakan untuk membuat endcoding
import seaborn as sns #seaborn untuk membuat heatmap/grafik berwarna
import matplotlib.pyplot as plt #pylot menampilkan heatmap
from sklearn.model_selection import train_test_split #diguakan memisahkan data train dan data test
from sklearn.linear_model import LogisticRegression #digunkan sebagai model MachineLearning
from sklearn.ensemble import RandomForestClassifier#digunan sebagai model Machine Learning
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score #untuk Metrix


"""============================= INISIALISASI DATA ==================================="""
print("\n============ DATA ================\n")

#Memanggil data dari Mongodb atau lebih tepatnya adalah mengkoneksikan ke Mongodb
""" 
Penjelasan :

Alasan kami memanggil atau mengkoneksikan Mongodb 
dikarenakan data sensor pH, suhu, tds atau nutrisi yang ada di File .ino dikirim ke Flask 
lalu dikirim ke Mongodb, agar data kami disimpan di database
"""

client = MongoClient('mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik')
#client adalah variabel yang berfungsi untuk mengkoneksikan Mongodb ke program ini, dan MongoClient adalah class dari library pymongo
database = client['Smart_Hidroponik'] #untuk memilih atau mengkoneksikan database yang sudah kami tambahkan
collection = database['Sensor'] #untuk memilih atau mengkoneksikan koleksi atau collection yang sudah kami tambahkan 

"""
Penjelasan :

Kami mendapatkan format link tersebut dari website Mongodb, 
kami mendapatkannya dari tombol connect yang terdapat di overview,
lalu kami menekan timbil drivers sehingga muncul format link:
mongodb+srv://<username>:<password>@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik
"""


