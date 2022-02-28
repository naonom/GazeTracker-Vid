import cv2
import os

from numpy import diff
import CornerToFrame


class Video():
    cap: cv2
    coutFrame: int
    width: int
    height: int

    def __init__(self, videoPath:str):
        self.cap = cv2.VideoCapture(videoPath)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if (self.cap.isOpened() == True):
            print("open video")
        self.coutFrame = 0

        self.toCorner = CornerToFrame.toPoint()
        self.toCorner.estimateCorner()

        #self.getPointX(c1=self.toCorner.corner1X,c2=self.toCorner.corner3X)


    def playVideo(self, dsize:int, frame:int):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, self.frame = self.cap.read()
        if ret == True:
            self.frame = cv2.resize(self.frame, dsize=(dsize, int(dsize*int(self.height)/int(self.width))))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        #cv2.imshow("video", self.frame)

    def playVideoOut(self, dsize:int, frame:int, gazeX:float, gazeY:float):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, self.frame = self.cap.read()
        if ret == True:
            #print(int(self.tiltX * gazeX + self.diffX))
            #print(int(self.tiltY * gazeY + self.diffY))
            cv2.rectangle(self.frame, pt1=(0, 0), pt2=(100, 100), color=(0,0,255), thickness=4)
            self.frame = cv2.resize(self.frame, dsize=(dsize, int(dsize*int(self.height)/int(self.width))))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        #cv2.imshow("video", self.frame)
        
    def endVideo(self):
        self.cap.release()
        cv2.destroyAllWindows()
       

