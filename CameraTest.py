import numpy as np
import cv2
from Image import *
from Utils import *
import time

WIDTH = 320
HEIGHT = 240

Images=[]
N_SLICES = 6

for _ in range(N_SLICES):
    Images.append(Image())

img = cv2.VideoCapture(0)
#ret = img.set(cv2.CAP_PROP_FPS, 30)
#ret= img.set(cv2.CAP_PROP_SATURATION, 0)
#ret = img.set(cv2.CAP_PROP_BRIGHTNESS, 0.61)
#ret= img.set(cv2.CAP_PROP_CONTRAST, 0.54)
#ret = img.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
#ret = img.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
ret = img.set(3,320)
ret = img.set(4,240)
skip = 30
while True:
    
    ret , frame = img.read()
    '''
    if not ret:
        print('cannot read camera')
        break
        
    print(frame)
    cv2.imshow("Vision Race", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            #cv2.destroyAllWindows()
            break
    '''
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
            break
        
        # command
        # get_cmd(Points[0][0], Points[1][0], Points[2][0], Points[3][0], Points[4][0], Points[5][0])
    else:
        print('not even processed')
    
img.release()
cv2.destroyAllWindows()
