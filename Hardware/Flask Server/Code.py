from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(_name_)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Udaya@1616',
    'database': 'medication_data'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return "Welcome to the Arduino Sensor Data API!"

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        barcode = request.json.get('barcode')
        temperature = request.json.get('temperature')
        humidity = request.json.get('humidity')
        if not barcode or not temperature or not humidity:
            return jsonify({'status': 'error', 'message': 'Missing barcode, temperature or humidity'}), 400
        print(f"Received data - Barcode: {barcode}, Temperature: {temperature}, Humidity: {humidity}")
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO records (barcode, temperature, humidity, timestamp) 
                   VALUES (%s, %s, %s, %s)"""
        timestamp = datetime.now()
        cursor.execute(query, (barcode, temperature, humidity, timestamp))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Data inserted successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
