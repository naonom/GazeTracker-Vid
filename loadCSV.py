import pandas as pd
from email import header

class CSVData():
    frameData:list[int]
    timeData:list[float]
    gazeX:list[float]
    gazeY:list[float]

    def __init__(self, csvPath:str):

        self.df = pd.read_csv(csvPath, encoding="SHIFT_JIS", usecols=[0, 2, 11, 12])
        self.frameData = self.df["frame"].tolist()
        self.timeData = self.df["timestamp"].tolist()
        self.gazeX = self.df["gaze_angle_x"].tolist()
        self.gazeX = self.df["gaze_angle_y"].tolist()

    def p(self):
        print("end load")
        #print(self.a[100])