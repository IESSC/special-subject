import glob
import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import paho.mqtt.publish as publish
import json
from datetime import datetime
from findmaxmin import findmax,findmin,rms
from numpy import mean, square
from selectdata import select
from normalize import nsdata
from Dstd import Dstd
# In[]讀取多個檔案並串接

all_files1 = glob.glob(os.path.join('D:\Spyder_StrainGauge_Data',"test",'D2*19*4131.csv'))
all_files2 = glob.glob(os.path.join('D:\Spyder_StrainGauge_Data',"test",'D2*draw*.csv')) 
all_data_frames = []
D1D2_files=[]
D1D2_files.append(all_files1[-2])
D1D2_files.append(all_files1[-1])
D1D2_files.append(all_files2[-2])
D1D2_files.append(all_files2[-1])
for file in D1D2_files:
    data_frame = pd.read_csv(file, index_col=None) 
    all_data_frames.append(data_frame)
    
data_frame_concat = pd.concat(all_data_frames, axis=1,ignore_index=False)
data_frame_concat.to_csv('DT_All_ouput.csv', index = False)

# In[]新增標題
header_list = ['DT_D1_1Strain_Gauge',
               'DT_D1_2Strain_Gauge',
               'DT_D2_1Strain_Gauge',
               'DT_D2_2Strain_Gauge']    

Add_header_list = pd.read_csv('DT_All_ouput.csv',
                         index_col=None,
                         header=None,
                         names=header_list)  
print(Add_header_list)

# In[]

data = pd.DataFrame(Add_header_list, index=None)
#data = pd.DataFrame(data_frame_concat)
data.to_csv('DT_All_ouput.csv', index = False)

data.plot(subplots=True, figsize=(10, 10),title="Strain Gauge")
plt.show()

# In[]
#= pd.DataFrame(columns=list(range(0,10)))
s1=select(data,0)
sp1=square(s1-mean(s1))
sp1.plot(subplots=True, figsize=(8, 5),title="Select_Strain Gauge1")
s1.to_csv('ST1_on.csv',index=False)
plt.show()

s2=select(data,1)
sp2=square(s2-mean(s2))
sp2.plot(subplots=True, figsize=(8, 5),title="Select_Strain Gauge2")
s2.to_csv('ST2_on.csv',index=False)
plt.show()

s3=select(data,2)
sp3=square(s3-mean(s3))
sp3.plot(subplots=True, figsize=(8, 5),title="Select_Strain Gauge3")
s3.to_csv('ST3_on.csv',index=False)
plt.show()

s4=select(data,3)
sp4=square(s4-mean(s4))
sp4.plot(subplots=True, figsize=(8, 5),title="Select_Strain Gauge4")
s4.to_csv('ST4_on.csv',index=False)
plt.show()

  


# In[]

all_rms=[]
all_rms.append(rms(s1))
all_rms.append(rms(s2))
all_rms.append(rms(s3))
all_rms.append(rms(s4))


# In[] 正規化訊號

st1=pd.read_csv('ST1_on.csv',index_col=None,header=None)
st2=pd.read_csv('ST2_on.csv',index_col=None,header=None)  
st3=pd.read_csv('ST3_on.csv',index_col=None,header=None) 
st4=pd.read_csv('ST4_on.csv',index_col=None,header=None) 

x_max1=st1.max(axis=0)
x_max1='{:f}'.format(x_max1[0])
x_max2=st2.max(axis=0)
x_max2='{:f}'.format(x_max2[0])
x_max3=st3.max(axis=0)
x_max3='{:f}'.format(x_max3[0])
x_max4=st4.max(axis=0)
x_max4='{:f}'.format(x_max4[0])

x_min1=st1.min(axis=0)
x_min1='{:f}'.format(x_min1[0])
x_min2=st2.min(axis=0)
x_min2='{:f}'.format(x_min2[0])
x_min3=st3.min(axis=0)
x_min3='{:f}'.format(x_min3[0])
x_min4=st4.min(axis=0)
x_min4='{:f}'.format(x_min4[0])

a=findmax(x_max1,x_max2,x_max3,x_max4)
b=findmin(x_min1,x_min2,x_min3,x_min4)
a=float(a)
b=float(b)


nst1=nsdata(st1,a,b)
nst2=nsdata(st2,a,b)
nst3=nsdata(st3,a,b)
nst4=nsdata(st4,a,b)

nst1.to_csv('NST1_on.csv',index=False)
nst2.to_csv('NST2_on.csv',index=False)
nst3.to_csv('NST3_on.csv',index=False)
nst4.to_csv('NST4_on.csv',index=False)

# In[] 計算標準差

# index Auto STart

all_std=[]
std_1=[]
for i in range(0,len(nst1),72):
    std1=nst1.iloc[i:72+i,0]
    rstd=np.std(std1)
    std_1.append(rstd)
    i=i+72
plt.hist(std_1)
plt.savefig('D:\\node-red_picture\\std_1.jpg') 
plt.show() 
#When working with paths that contain backslashes, 
#you either need to use two backslashes, or use the r'' form to prevent interpreting of escape sequences. 
#For example, 'C:\\Program Files\\...' or r'C:\Program Files\...'.    
all_std.append(np.std(std_1))

std_2=[]
for i in range(0,len(nst2),72):
    std2=nst2.iloc[i:72+i,0]
    rstd=np.std(std2)
    std_2.append(rstd)
    i=i+72    
plt.hist(std_2)
plt.savefig('D:\\node-red_picture\\std_2.jpg') 
plt.show()
all_std.append(np.std(std_2))
 
std_3=[]
for i in range(0,len(nst3),72):
    std3=nst3.iloc[i:72+i,0]
    rstd=np.std(std3)
    std_3.append(rstd)
    i=i+72      
plt.hist(std_3)
plt.savefig('D:/node-red_picture/std_3.jpg') 
plt.show()
all_std.append(np.std(std_3))

std_4=[]
for i in range(0,len(nst4),72):
    std4=nst4.iloc[i:72+i,0]
    rstd=np.std(std4)
    std_4.append(rstd)
    i=i+72      
plt.hist(std_4)
plt.savefig('D:/node-red_picture/std_4.jpg') 
plt.show()    
all_std.append(np.std(std_4))

#all_std.append(np.std(std_1))
#all_std.append(np.std(std_2))
#all_std.append(np.std(std_3))
#all_std.append(np.std(std_4))



# In[] 




# In[]
    
host = "m10.cloudmqtt.com"
portNo = 17423

# In[]

var = 1
while var == 1:
    time=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    msg = {"time1":time,"time2":time,"time3":time,"time4":time,"time5":time}
    jmsg = json.dumps(msg, ensure_ascii=False)
    publish.single("mislab/mqtt/stdtime", jmsg, hostname = host)
    

    msg = {"rms1":all_rms[0],"rms2":all_rms[1],"rms3":all_rms[2],"rms4":all_rms[3]}
    jmsg = json.dumps(msg, ensure_ascii=False)
    publish.single("mislab/mqtt/std", jmsg, hostname = host)


# In[]

#msgs = [{'topic':"mislab/mqtt/std",
#         'payload':"Donate 1"
#         ''},
#        ("mislab/mqtt/test","Donate 10",0, False)]
#publish.multiple(msgs, hostname = host)



#publish.single("mislab/mqtt/callback", jmsg, hostname = host)

# In[]

#import numpy as np
#import matplotlib.pyplot as plt


#theta = np.linspace(0.0, 360, num=5) #θの範囲を 0-8π ラジアン(4周分)とする
#r = 0.5*theta   ## 極方程式を指定する。
#plt.polar(theta,r) # 極座標グラフのプロット

#plt.show()



# In[]
