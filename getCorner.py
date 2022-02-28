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

    def saveTxt(self):
    
        path_w="corner2.txt"
        text:list=[]
        text.append(str(self.leftupX)+"\n")
        text.append(str(self.leftupY)+"\n")

        text.append("\n")

        text.append(str(self.leftdownX)+"\n")
        text.append(str(self.leftdownY)+"\n")

        text.append("\n")

        text.append(str(self.rightupX)+"\n")
        text.append(str(self.rightupY)+"\n")

        text.append("\n")

        text.append(str(self.rightdownX)+"\n")
        text.append(str(self.rightdownY)+"\n")
        with open(path_w, mode="w") as f:
            f.write("test")
            for w in text:
                f.write(w)
        
