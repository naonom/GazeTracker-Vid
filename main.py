import tkinter as tk
from tkinter.constants import LEFT, NUMERIC
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk, ImageOps
import datetime
import os
import gazetracker as gt
import makedata
import serial

import loadVideo
import loadCSV


class Application(tk.Frame):
        #ls -l /dev/tty.*

        pointing: bool = False
        xCenter: float = 0.0
        yCenter: float = 0.0

        def __init__(self, master=None):
                super().__init__(master)
                self.master.geometry("720x450")
                self.master.title("GazeTracker")
                self.master.resizable(width=False, height=False)
                #self.gazetrack = gt.GazeTrack(0)

                self.inVideo = loadVideo.Video("OpenFace-master/patern1/patern1_In.mp4")
                self.csvData = loadCSV.CSVData("OpenFace-master/patern1/patern1_In.csv")

                self.width = self.inVideo.width
                self.height = self.inVideo.height

                self.xParam: list = [0, 0, 0]
                self.yParam: list = [0, 0, 0]

                self.xdis: float = 0.0
                self.ydis: float = 0.0
                self.dis: int = 50

                self.frame = 0


                self.create_frame()
                self.create_widget()
                self.delay = 16
                self.play_video()

                try:
                        self.com = '/dev/tty.usbserial-3552041E93'
                        self.ser = serial.Serial(self.com, 9600, timeout=None)
                        self.serialCheck()
                except:
                        self.com = None

        def create_frame(self):
                #フレームの作成frame1 = 背景 frame2 = ラベル
                self.frame1 = tk.Frame(self.master, width=720, height=505, bg="#C4C4C4")
                self.frame1.place(x=0, y=0)
                self.frame2 = tk.Frame(self.master, width=720, height=40, bg="#3F3F3F")
                self.frame2.place(x=0, y=0)
                self.canvas = tk.Canvas(self.frame1, width=720, height=480)
                self.canvas.pack()
        
        def create_widget(self):
                #Labelの生成
                b_camera = tk.Button(self.frame2, text = "camera", width=3, command=self.setup_window)
                b_camera.grid(row=0, column=0, padx=2, pady=2, sticky=tk.E)
                e_camera = tk.Button(self.frame2, text = "Exit", width=3, command=self.endApp)
                e_camera.grid(row=0, column=1, padx=2, pady=2, sticky=tk.E)

        def setup_window(self):
                #self.gazetrack.takePhoto()
                if self.subWin == None or not self.subWin.winfo_exists():
                        self.subWin = tk.Toplevel()
                        self.subWin.resizable(width=False, height=False)
                        self.subWin.geometry("350x150")
                        
        def get_setting(self):
                try:
                        print("for demo")
                except:
                        return

        def close_sub(self):
                self.subWin.destroy()

        def key_event(self, e):
                key = e.keysym
                if key == "p":
                        self.takePhoto()
                        self.pointing = False
                if key == "s":
                        self.setup_window()
                if key == "e":
                        self.endApp()
                        #self.makedata.closeFile()
                
        def endApp(self):
                self.master.destroy()

        def takePhoto(self):
                print("take")
                self.pointing = True
                if not os.path.exists("Photo"):
                        os.mkdir("Photo")
                
                nowtime = datetime.datetime.now()

                self.outputimage.save("Photo/" + str(nowtime) + ".jpg")
                self.norectimage.save("Photo/" + str(nowtime) + "noRect.jpg")
        

        def play_video(self):
                self.inVideo.playVideo(dsize=720, frame=self.frame)
                #cv2.imshow("video", invidImage)
                self.invidImage = PIL.Image.fromarray(self.inVideo.frame)
                self.invidPhoto = PIL.ImageTk.PhotoImage(image=self.invidImage)
                self.canvas.create_image(0, 30, image=self.invidPhoto, anchor=tk.NW)

                self.frame +=1

                #10ms
                self.master.after(self.delay, self.play_video)
        
        def serialCheck(self):
                if self.com is not None:
                        result = self.ser.read_all()
                        if result == b"P":
                                self.takePhoto()
                self.master.after(self.delay, self.serialCheck)

def main():
        root = tk.Tk()
        app = Application(master=root)
        app.subWin = None
        root.bind("<KeyPress>", app.key_event)
        app.mainloop()

if __name__ == "__main__":
        main()