import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folde
vehicles_folder_count = 0
cap = cv2.VideoCapture(0)
  
# loop runs if capturing has been initialized.
while 1: 
  
    # reads frames from a camera
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('img',img)
  
    # convert to gray scale of each frames

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
# Display an image in a window
    # Display an image in a window
    #cv2.imshow('img',img)
  
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
  
# Close the window
cap.release()
  
# De-allocate any associated memory usage
cv2.destroyAllWindows() 


print("Total current count", vehicles_folder_count)
