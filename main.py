#this is a screen recoder using python
# we are gonna take a screenshot for every millisecond and then merge them all together
#importing the modules
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
#captures the entire screen  and we can even give the custom dimensions
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)
#Taking the inputs
duration=int(input("Enter the Duration of the Screen Recording in minutes  "))
duration=duration*60
duration=duration+60
name=input("Enter the name of the File  ")
name=name+".avi"

#format of the mp4 file
f=cv2.VideoWriter_fourcc(*"MPEG")
#location of the file  and name  and dimensions
output=cv2.VideoWriter(name,f,23,dim)
#Timings ie the start time and end time
now_start_time=time.time()
#duration , we add plus 4 seconds so that the code gets compiled
dur=duration
end_time=now_start_time+dur
#capturing the viedo
while True:
    img=pyautogui.screenshot()
    frame_1=np.array(img)
    frame_2=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame_2)
    #Stopping condition
    c_time=time.time()

    if c_time>end_time:
        break
output.release()
print("---- END----")
