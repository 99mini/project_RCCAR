import time

import cv2
import numpy as np
import serial

from Image import *
from Utils import *

WIDTH = 320
HEIGHT = 240
TOLERANCE = 145
TURN_MAX = 190
TURN_MID = 90

### cmd define
direction = 0

def in_tolerance(n):
    if n < -TOLERANCE:
        return False
    if n > TOLERANCE:
        return False
    return True

def get_cmd(y1, y2, y3, y4, y5, y6):
    
    num_valid = 6
    
    y1 -= WIDTH/2
    y2 -= WIDTH/2
    y3 -= WIDTH/2
    y4 -= WIDTH/2
    y5 -= WIDTH/2
    y6 -= WIDTH/2
    
    master_point = 0
    
    # +: right
    # -: left
    if in_tolerance(y1) == False:
        num_valid -= 1
        y1 = 0
    if in_tolerance(y2) == False:
        num_valid -= 1
        y2 = 0
    if in_tolerance(y3) == False:
        num_valid -= 1
        y3 = 0
    if in_tolerance(y4) == False:
        num_valid -= 1
        y4 = 0
    if in_tolerance(y5) == False:
        num_valid -= 1
        y5 = 0
    if in_tolerance(y6) == False:
        num_valid -= 1
        y6 = 0
    
    master_point = 2.65 * (y1 * 0.7 + y2 * 0.85 + y3 + y4 * 1.1 + y5 * 1.2 + y6 * 1.35) / (num_valid + 0.1)

    master_point += y1 * 0.5
    master_point += y2 * 0.4
    master_point += y3 * 0.3
    master_point -= y4 * 0.4
    master_point -= y5 * 0.5
    master_point -= y6 * 0.6

    # back
    if num_valid < 2:
        direction = 'B'
    else:
        direction = 'G'
        '''
        if master_point > TURN_MID and master_point < TURN_MAX :
            direction = 'l'
        if master_point < -TURN_MID and master_point > -TURN_MAX :
            direction = 'r'
        '''
        if master_point >= TURN_MAX :
            direction = 'L'
        if master_point <= -TURN_MAX :
            direction = 'R'

    cmd = ("%c\n" % (direction)).encode('ascii')

    print(">>> master_point:%d, cmd:%s" % (master_point, cmd))
    
    ser.write(cmd)
    print("send")
    # read cmd from arduino and print it    
    read_serial = ser.readline()
    print("<<< %s" % (read_serial))


### setting arduino
base_path = '/dev/serial/by-id/'
by_id = 'usb-Arduino__www.arduino.cc__0043_758303334383510102E1-if00'
ser = serial.Serial(base_path+by_id, 9600)

print('start')
time.sleep(3)

### settting camera
Images=[]
N_SLICES = 6

for _ in range(N_SLICES):
    Images.append(Image())

img = cv2.VideoCapture(0)
ret = img.set(cv2.CAP_PROP_FPS, 30)
ret= img.set(cv2.CAP_PROP_SATURATION, 0)
ret = img.set(cv2.CAP_PROP_BRIGHTNESS, 0.61)
ret= img.set(cv2.CAP_PROP_CONTRAST, 0.54)
ret = img.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
ret = img.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

skip = 30

while True:

    ret , frame = img.read()

    if skip > 0:
        skip -= 1
    elif frame is not None:
        skip = 6
        #이미지를 조각내서 윤곽선을 표시하게 무게중심 점을 얻는다
        Points = SlicePart(frame, Images, N_SLICES)
        
        print('Points : ', Points)
        print()
           
        #조각난 이미지를 한 개로 합친다
        fm = RepackImages(Images)
        
        #완성된 이미지를 표시한다
        cv2.imshow("Vision Race", fm)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            
        
        # command
        get_cmd(Points[0][0], Points[1][0], Points[2][0], Points[3][0], Points[4][0], Points[5][0])
    else:
        print('not even processed')

