import cv2
#import numpy as np


position = []


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Camera")

#yellow
lower = (30,70, 70)
upper = (133,255,255)

#red
lower = (10,27, 51)
upper = (7,155,200)

#green
lower = (30,90, 110)
upper = (62,205,190)


while cam.isOpened():
    ret, image = cam.read()
    blurred = cv2.GaussianBlur(image, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    
    mask = cv2.inRange(hsv,lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
        if radius > 10:
            cv2.circle(image, (int(curr_x), int(curr_y)), 5,
                       (0, 255, 255), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), 5,
                       (255, 0, 0), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), int(radius),
                       (255, 0, 0), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), 5,
                       (255, 165, 0), 2)
            cv2.circle(image, (int(curr_x), int(curr_y)), int(radius),
                       (255, 165, 0), 2)
    
    
    
    
    
    cv2.imshow("Camera", image) 
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break




cam.release()
cv2.destroyAllWindows()