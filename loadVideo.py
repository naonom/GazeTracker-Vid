import cv2
import os

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
            #print(str(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        self.coutFrame = 0

    def playVideo(self, dsize:int, frame:int):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, self.frame = self.cap.read()
        if ret == True:
            self.frame = cv2.resize(self.frame, dsize=(dsize, int(dsize*int(self.height)/int(self.width))))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        #cv2.imshow("video", self.frame)
        
    def endVideo(self):
        self.cap.release()
        cv2.destroyAllWindows()
       

