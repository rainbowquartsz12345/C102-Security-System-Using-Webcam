import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    vcobj = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = vcobj.read()
        imgname = "img"+str(number)+".png"
        cv2.imwrite(imgname, frame)
        start_time = time.time
        result = False
    return imgname
    vcobj.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token = "sl.BHgO9nNa00rhOH5ctb6EPR6fyru7lcIYFMp6WA2EvaTMskps5lKfHuPFdXZY13nyKo7emK0RouwIDTHXNOHWKCOWV_xez_zGdo0rrJy_QMzoXEpGYwyWVqn11kRpRv88PI2AgEZK3vI"
    file = img_name
    file_from = file
    file_to = "/C102Snaps/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
         # to resolve the path errors, last parameter is added
        dbx.files_upload(f.read() ,file_to, mode = dropbox.files.WriteMode.overwrite  )
        print("File Uploaded")
    
def main():
    while(True):
        if( (time.time() - start_time ) >=5   ):
            name = take_snapshot()
            uploadFile(name)
main()



