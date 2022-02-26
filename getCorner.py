import os

class DitectCorner():
    def __init__(self):
        self.leftupX: float=0.0
        self.leftdownX: float=0.0
        self.rightupX: float=0.0
        self.rightdownX: float=0.0

        self.leftupY: float=0.0
        self.leftdownY: float=0.0
        self.rightupY: float=0.0
        self.rightdownY: float=0.0

        self.rawDataX: float=0.0
        self.rawDataY: float=0.0

        self.count: int=0

    def reset(self):
        self.rawDataX=0.0
        self.rawDataY=0.0

        self.count=0

    def getData(self, angleX:float, angleY:float):
        self.count+=1
        self.rawDataX=(self.rawDataX+angleX)/self.count
        self.rawDataY=(self.rawDataY+angleY)/self.count

    def setData(self, corner:str):
        if corner == "leftup":
            self.leftupX=self.rawDataX
            self.leftupY=self.rawDataY
        if corner == "leftdown":
            self.leftdownX=self.rawDataX
            self.leftdownY=self.rawDataY
        if corner == "rightup":
            self.rightupX=self.rawDataX
            self.rightupY=self.rawDataY
        if corner == "rightdown":
            self.rightdownX=self.rawDataX
            self.rightdownY=self.rawDataY

    def showData(self):
        print(self.count)
        print(self.leftupX)
        print(self.leftupY)