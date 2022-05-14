import cv2
import time
import random
def take_snapshot():
    number=random.randint(0,100)
    if(number<0):
        number=1
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    print('Snapshot Taken')
    return img_name
    print('snapshot stored')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()
