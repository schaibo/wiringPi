import time
import serial
import sys 

ser=serial.Serial('/dev/ttyUSB0',57600,parity=serial.PARITY_NONE)  

def main():
  if ser.isOpen == False:  
        ser.open()  
  #ser.write(b"serial turn on")  

  while True:  
        size = ser.inWaiting()  
        if size != 0:  
             response = ser.read(size)  
             data = str(response)
             #print('data:'+data)
             item = data.split(",")
             print(item)  
             pm25 = item[1]
             fd = item[2]
             co2 = item[3]
             temp = item[4]
             hd = item[5] 
             #print('pm25:'+pm25 + "fd:" + fd)  
             ser.flushInput()  
             time.sleep(0.1)

if __name__ == '__main__':

  try:  
     main()
  except KeyboardInterrupt:  
     if ser != None:
         ser.close() 
