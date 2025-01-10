import serial #communicate with arduino
import requests #send data to flask sever
import json

serial_port = 'COM3'  
baud_rate = 9600  #speed data is transmitted
flask_server_url = "http://127.0.0.1:5000/post_data"
ser = serial.Serial(serial_port, baud_rate) 

while True:
    if ser.in_waiting > 0:
        
        datas = ser.readline().decode('utf-8').strip()

        
        try:
            temperature, humidity = datas.split(',')

            
            payload = {                 
                "temperature": float(temperature),
                "humidity": float(humidity),
            }
           
            response = requests.post(flask_server_url, json=payload)

            
            if response.status_code == 200:
                print(f"Successfully posted: {json.dumps(payload)}")
            else:
                print(f"Failed to post data: {response.text}")

        except ValueError:
            print(f"Invalid data format received: {datas}")

