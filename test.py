import serial
import binascii
import crc16

SMLSTART = bytes([0x1B, 0x1B, 0x1B, 0x1B, 0x01, 0x01, 0x01, 0x01])
SMLSTOP = bytes([0x1B, 0x1B, 0x1B, 0x1B, 0x1A])
index = 0
reading = True
data = SMLSTART
ser = serial.Serial('/dev/ttyUSB0')
if(ser.read_until(SMLSTART, 800)):
    while(reading):
        b = ser.read(1)
        data = data + b
        if b == SMLSTOP[index:index+1]:
            index = index + 1
        if index >= 5:
          data = data + ser.read(3)
          reading = False
ser.close() 
print(hex(crc16.crc16xmodem(data[0:len(data)-2])))
print(data.hex())
print(data[len(data)-2:].hex())
