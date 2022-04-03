from curses import raw


class toPoint():
    def __init__(self):
        self.framePointX:int=0
        self.framePointY:int=0
        self.cornerData:list=[]
        try:
            path="corner2.txt"
            with open(path) as f:
                rawdata=f.read()
                self.cornerData=rawdata.split("\n")
                self.cornerData.remove("")
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            self.cornerData=["0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"]
            return

    def estimateCorner(self):
        testData=[float(s) for s in self.cornerData]
        testData=[round(s, 3) for s in testData]

        print(testData)
        #corner1
        self.corner1X=round((testData[0]+testData[2])/2, 3)
        self.corner1Y=round((testData[1]+testData[7])/2, 3)

        #corner3
        self.corner3X=round((testData[6]+testData[4])/2, 3)
        self.corner3Y=round((testData[3]+testData[5])/2, 3)



    

