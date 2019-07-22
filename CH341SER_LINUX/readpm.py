import time
import serial
import sys 
import pymysql
import datetime

ser=serial.Serial('/dev/ttyUSB0',57600,parity=serial.PARITY_NONE)  

def getdata():
  try :
    if ser.isOpen == False:  
        ser.open()  
    #ser.write(b"serial turn on")  
    print("serial turn on")

    while True:
      size = ser.inWaiting()  
      if size != 0:  
        response = ser.read(size)  
        data = str(response)
        item = data.split(",")
        print(item)  
        pm25 = item[1]
        fd = item[2]
        co2 = item[3]
        temp = item[4]
        hd = item[5] 
        #print('pm25:'+pm25 + "fd:" + fd)  
        ser.flushInput()  
        sql = "DELETE from  FD where 0=0"
        updb_pm(sql)
        sql1 = "INSERT INTO FD VALUES ('" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) +"',"+pm25+","+fd+","+co2+","+temp+","+hd+")"
        #print(sql1)
        updb_pm(sql1)
        break
    ser.close 
  except Exception as e:
    print("出现EXCEPTION！60秒钟后重试……")
    print(("Exception："+str(e)))
    time.sleep(600)
    # 出现异常则过一段时间重新执行此部分
    getdata()
def updb_pm(sql):
   #连接mysql
   conn = pymysql.connect(host='z-haibo.win',user='root',password='123456',database='weather',use_unicode=True, charset="utf8")
   cursor = conn.cursor()
   cursor.execute(sql)
   conn.commit()
   #print("insert database succ !")
   cursor.close()
   conn.close()

if __name__ == '__main__':

   try:
     while True:
         print("开始工作！")
         getdata()
         print("完成…")
         time.sleep(1800) 
   except KeyboardInterrupt:
     if ser != None:
         ser.close()
