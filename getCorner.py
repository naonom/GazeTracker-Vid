import os
import statistics

class DitectCorner():
    rawDataX: list = []
    rawDataY: list = []

    def __init__(self):
        self.leftupX: float=0.0
        self.leftdownX: float=0.0
        self.rightupX: float=0.0
        self.rightdownX: float=0.0

        self.leftupY: float=0.0
        self.leftdownY: float=0.0
        self.rightupY: float=0.0
        self.rightdownY: float=0.0


    def reset(self):
        try:
            self.rawDataX.clear()
            self.rawDataY.clear()
        except:
            print("raw data is null")


    def getData(self, angleX:float, angleY:float):
        self.rawDataX.append(angleX)
        self.rawDataY.append(angleY)

    def setData(self, corner:str):
        try:
            dataX = statistics.mean(self.rawDataX)
            dataY = statistics.mean(self.rawDataY)
            if corner == "leftup":
                self.leftupX=dataX
                self.leftupY=dataY
            if corner == "leftdown":
                self.leftdownX=dataX
                self.leftdownY=dataY
            if corner == "rightup":
                self.rightupX=dataX
                self.rightupY=dataY
            if corner == "rightdown":
                self.rightdownX=dataX
                self.rightdownY=dataY
        except:
            print("set data fail")

    def showData(self):
        print(self.leftupX)
        print(self.leftupY)