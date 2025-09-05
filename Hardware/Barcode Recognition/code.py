import sys
import cv2
import mysql.connector
from pyzbar.pyzbar import decode

class BarcodeRecognition:
    def __init__(self):
        self.known_barcodes = set()  # Keep track of detected QR codes
        self.db_connection = None
        self.db_cursor = None

    def connect_to_database(self):
        
        host = 'localhost'
        username = 'root'
        password = 'Sanjey@27'
        database = 'med'  # Name of your database

        try:
            self.db_connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password,
                database=database
            )
            self.db_cursor = self.db_connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL database: {err}")
            sys.exit()

    def run_recognition(self):
        
        self.connect_to_database()
        
        video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not video_capture.isOpened():
            sys.exit('Unable to open web54cam...')

        while True:
            ret, frame = video_capture.read()
           
            barcodes = decode(frame)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
               
                if barcode_data not in self.known_barcodes:
                    self.known_barcodes.add(barcode_data)
                    
                    self.db_cursor.execute(
                        "SELECT * FROM medicine WHERE barcode_id = %s", (barcode_data,))
                    result = self.db_cursor.fetchone()

                    if result:
                        print(f"Detected QR code: {barcode_data}")
                        print("Related data:")
                        for key, value in result.items():
                            print(f"{key}: {value}")
                    else:
                        print(f"No match found for barcode: {barcode_data}")

            cv2.imshow('Barcode Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    br = BarcodeRecognition()
    br.run_recognition()
