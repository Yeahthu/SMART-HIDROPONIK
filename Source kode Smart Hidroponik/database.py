
from flask import Flask, request, jsonify # Memanggil flask untuk membuat local server, request untuk dan jsonify
from pymongo import MongoClient as mongo # Untuk mengakses database menggunakan mongo 
from pymongo.errors import ConnectionFailure 

web = Flask(__name__) # untuk inisialisasi flask 

# Koneksi ke MongoDB
url_database = "mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik"

@web.route('/cek_url')
def cek_url():
    try:
        # Inisialisasi client MongoDB
        client = mongo(url_database)
        
        # Pilih database
        db = client.Smart_Hidroponik
        
        # Pilih koleksi
        collection = db.Sensor_TDS
        
        # Coba lakukan operasi sederhana untuk memastikan koneksi
        sample_doc = collection.find_one()
        
        if sample_doc:
            return "Koneksi berhasil", 200
        else:
            return "Koneksi isoh, nanging ijek kosong", 200
    except ConnectionFailure:
        return "Koneksi ke MongoDB gagal sabar nggih , wkwkwk ", 500

if __name__ == '__main__':
    web.run(debug=True)



