import cv2

cap = cv2.VideoCapture("OpenFace-master/patern1/patern1_In.mp4")

if (cap.isOpened()== False):  
  print("ビデオファイルを開くとエラーが発生しました") 

while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow("Video", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    
    else:
        break

cap.release()

cv2.destroyAllWindows()