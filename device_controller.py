import serial
import time

def init_serial_connection():
    try:
        global ser
        ser = serial.Serial('/dev/ttyUSB0', baudrate='115200', timeout=4)
        time.sleep(4)
        return ser
    except serial.SerialException as e:
        print(f"Error initializing serial connection: {e}")
        return None

def send_message(ser, message):
    try:
        ser.write((message + '\n').encode())
    except Exception as e:
        ser.write(("Exited\n").encode())
        print(f"Error sending message: {e}")
