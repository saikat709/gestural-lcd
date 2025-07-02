import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate='115200', timeout=2) 
time.sleep(3)

try:
    message = "Hello...!"
    while True:
        ser.write((message + '\n').encode())
        print("Sent:", message)
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
