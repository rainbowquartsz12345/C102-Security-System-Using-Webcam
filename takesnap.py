import cv2

def take_snapshot():
     #initializing cv2
     videoCaptureObj = cv2.VideoCapture(0)
     result  = True
     while(result):
          #read the frames while the camera is on
          # ret is a dummy variable returns boolean value, if something is being returned or not          
          ret,frame = videoCaptureObj.read()
          #cv2.imwrite() method is used to save an image to any storage device
          cv2.imwrite('chloe.jpg' , frame)
          result = False

     #closes the camera
     videoCaptureObj.release()
     #close all windows that might have opned during this process
     cv2.destroyAllWindows()

take_snapshot()