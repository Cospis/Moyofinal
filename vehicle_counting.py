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
    images_folder = glob.glob("image/*.jpg")

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

        cv2.imshow("Cars", img)
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
    
    #src = os.getcwd()
    #filename = str(os.listdir(src + "/image"))
    #source = str(src + filename[0])
    #dest = str(src+  "\Counted\\"+ filename[0])
    #print(source)
    #print(dest)
    #print(filename[0])
#    os.rename(filename,dest )
    print("Moved")
print(Count())
move()
