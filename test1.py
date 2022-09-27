import cv2
from datetime import datetime
import time
import cv2
import glob
import os
import shutil
from pathlib import Path
def Count():
    from vehicle_detector import VehicleDetector

# Load Veichle Detector
    vd = VehicleDetector()

# Load images from a folder
    images_folder = glob.glob("image/*.png")

    vehicles_folder_count = 0

# Loop through all the images
    for img_path in images_folder:
        print("Img path", img_path)
        img = cv2.imread(img_path)

        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)

    # Update total count
 #       vehicles_folder_count += vehicle_count

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        #cv2.imshow("Cars", img)
        cv2.waitKey(1)
        return vehicle_count

def move():
    src = os.getcwd()
    source = str(src + "\image\\")
    dest = str(src+  "\Counted\\")

    files = os.listdir(source)
    files.sort()
    for f in files:
        src = source+f
        dst = dest+f
        shutil.move(src,dst)

def image():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    Begin = time.time()
    while True:
        start = time.time()
        diff = start-Begin
        diff = round(diff)
        ret, frame = cam.read()
        #if not ret:
         #   cam.release()
          #  cam = cv2.VideoCapture(0)
           # continue
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            print("Escape hit, closing...")
            break
    #print(diff)
        if (diff== 5):
            for i in range(1):
                now = datetime.now()
                time_date = now.strftime("%d%m%Y%H%M%S")
                img_name = "image/Image_{}.png".format(time_date)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(time_date))
                break
            break
    cam.release()

    cv2.destroyAllWindows()
while True:
    image()
    print(Count())
    move()
