# script to send nsconn data to influxdb

# pip install influxdb 
from influxdb import InfluxDBClient
from datetime import datetime
import socket
import json

def influxFormat(obj):

  data = {}

  pythonObj = json.loads(obj)
  #access elements in the object
  
 # this was disabled as rawwav is massively slowing down the
 # script due to the high volume of objects
 # uncomment at your own peril
 # if "raweegpower" in pythonObj:
  #  rawwav = pythonObj['raweegpower']
   # 
    #data = {
     # "measurement": "raweegpower",
      #"time": datetime.now(),
      #"fields": {
       #   'rawwav': rawwav
      #}
    #}
    
  if "attention" in pythonObj:
    attention = pythonObj['attention']   
    data = {
      "measurement": "eSense",
      "time": datetime.now(),
      "fields": {
          'attention': attention
      }
    }
  elif "meditation" in pythonObj:
    meditation = pythonObj['meditation']   
    data = {
      "measurement": "eSense",
      "time": datetime.now(),
      "fields": {
          'meditation': meditation
      }
    }  
  elif "poorsignal" in pythonObj:
    poorsignal = pythonObj['poorsignal']   
    data = {
      "measurement": "poorsignal",
      "time": datetime.now(),
      "fields": {
          'poorsignal': poorsignal
      }
    }
    
  return data
  #json_payload.append(data)



s = socket.socket()
self = socket.gethostname()
port = 9192
s.connect((self,port))
outString = []

client = InfluxDBClient('localhost', 8086, 'yourusername', 'yourpassword', 'nsconn')
client.switch_database('nsconn')


pCount = 0
jObj = ""
while True:
  byte = s.recv(1)
  #print(byte.decode("utf-8"))
  if byte.decode("utf-8") == '{':
    pCount = pCount+1
    jObj = jObj + byte.decode("utf-8")
  elif byte.decode("utf-8") == '}':
    pCount = pCount-1
    jObj = jObj + byte.decode("utf-8")
    if pCount == 0:
      printo = influxFormat(jObj)
      print(printo)
      outString.append(printo)
      client.write_points(outString)
      jObj = ""
      continue
  else:
    jObj = jObj + byte.decode("utf-8")




