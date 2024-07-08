
# ''' SMART HIDROPONIK || MERA X'''

""" ================================ LIBRARY ================================="""
from flask import Flask, request, jsonify # Memanggil flask untuk membuat local server, request untuk dan jsonify
from pymongo import MongoClient as mongo # Untuk mengakses database menggunakan mongo 
from pymongo.errors import ConnectionFailure 
from datetime import datetime as dt # Datetime berfungsi agar dapat menampilkan waktu


app = Flask(__name__) # untuk inisialisasi flask 

""" ============================ MONGO (DATABASE) ====================================="""
# Koneksi ke MongoDB
url_database = "mongodb+srv://SmartHidroponik:MERA_X@smarthidroponik.hdetbis.mongodb.net/?retryWrites=true&w=majority&appName=SmartHidroponik"
client_database = mongo(url_database) #klien dari database yang sudah kami buat
database = client_database.Smart_Hidroponik #daabase yang kami buat
koleksi_database = database.Sensor_TDS #koleksi_database ini berguna untuk menyimpan data perbagian

"""=============================== MENDAPATKAN DATA  ================================="""
# @web.route("/Kirim_data",methods=["POST"])
# def kirim_data():
#     data = request.get_json()
@app.route('/dapat_data', methods=['POST'])
def dapat_data():
    data = request.get_json()
    waktu = dt.now().strftime("%d-%m-%Y ----- %H:%M:%S")

    data['waktu'] = waktu

    ''' ======= DATA PH =========='''
    if 'pH' and 'tds' in data: 
        data['pH'] = float(data['pH'])
        data['tds'] = float(data['tds'])
        data_ada = koleksi_database.find_one()

        if data_ada:
            return jsonify({"Pemberitahuan": "Data telah tersedia"}), 200
        else:
            koleksi_database.insert_one(data)
            return jsonify({"Pemberitahuan": "Data disisipkan"}), 201
        
    elif 'tds' in data:
        data_ada = koleksi_database.find_one()
        
    else:
        return jsonify({"error": "Tidak ada data, mohon cek kembali"}), 400


''' ======= KONVERSI OBJECT_ID =========='''
def konversi_objectid(data):
    if isinstance(data, list):
        for item in data:
            if '_id' in item:
                item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        if '_id' in data:
            data['_id'] = str(data['_id'])
    return data

@app.route('/sensor/data', methods=['GET'])
def get_data():
    data = list(koleksi_database.find())  # Fetch data from MongoDB
    data = konversi_objectid(data)  # Convert ObjectId to string

    return jsonify(data), 200

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
