import time
import cv2
def capture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    cv2.imshow("test", frame)

    time.sleep(2)
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
while True:
    
    capture()
    time.sleep(3)

