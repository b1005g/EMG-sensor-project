import serial
import re

num = 0;
ser = serial.Serial() # 시리얼을 연결한다.
ser.port = 'COM5' # 아두이노가 연결된 포트
ser.baudrate = 9600 # baudrate를 지정해줄 수 있다.

# baudrate를 모른다면 연결된 serial을 불러와서 확인할 수 있다.
# print(ser)

ser.timeout = 1 #시리얼에 데이터를 불러올 때 지정하는 딜레이

# 시리얼을 열어준다.
ser.open()

# 데이터를 저장할 공간을 만들어주었다.
data3 = []
data2 = []
# 반복해서 데이터를 출력하기 위해 while 을 만들어주었다.
while True:

  data = ser.readline() # serial에 출력되는 데이터를 읽어준다.
  # print(data)
  data2 = re.findall("\d{3}",str(data))
  # data2 = data[int(0)].substring[3,6] # byte 형태로 출력되는 데이터를 \ 로 나눠서 입력받는다. (센서마다 다름)
  # data3 = int(data2, 16)  # convert hex to decimal (16진법으로 출력되는 데이터를 10진법으로 바꿔준다)
  data2 = list(map(int, data2))
  data3.append(data2) # 출력된데이터를 data3에 저장한다.
  # enumerate(data3)
  # print(data2) #저장되는 데이터를 확인하고 data3의 크기가 100을 넘어가면 while을 끝낸다.
  
  
  list2 = []
  MAX_A = 700;

  # data3 = list(map(int, data3))
  
  if len(data3) > 100:
    print(len(data3))
    while data3[-1] > 420:
      list2.append(data3[-1])
      print(list2)
      if len(list2) > 100:
           AVG = sum(list2,0)/len(list2)
           print(AVG)
      if   AVG > MAX_A * 0.95 :
          print("100")
      elif AVG > MAX_A * 0.9 :
          print("90")
      elif AVG > MAX_A * 0.85 :
          print("80")
      elif AVG > MAX_A * 0.8 :
          print("70")
      elif AVG > MAX_A * 0.75 :
          print("60")
      elif AVG > MAX_A * 0.7 :
          print("50")
      else:
          print("0")  

# if len(data2) > 100:
   # break
ser.close() # serial
