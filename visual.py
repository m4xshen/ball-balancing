import cv2
import numpy as np

def hough(image):
    # Convert to grayscale.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (17,17), 0)
    canny_image = cv2.Canny(blurred_image, 80, 95)
    
    circles = cv2.HoughCircles(image=canny_image, method=cv2.HOUGH_GRADIENT,dp=1, minDist=30, param1 = 70,param2 = 30, minRadius = 40, maxRadius = 400)

    if circles is not None:

        # Convert the circle parameters x, y and r to integers.
        circles = np.uint16(np.around(circles))

        for circle in circles[0, :]:
            x, y, r = circle[0], circle[1], circle[2]

            # Draw the circumference of the circle.
            cv2.circle(image, (x, y), r, (0, 0, 255), 7) # draw circumference of circle
            cv2.circle(image, (x, y), 1, (0, 0, 255), 5) # draw center of circle
          
        print("Centroid: "+str((x, y)))
    return image

cap = cv2.VideoCapture(0) # choose camera index

while cap.isOpened():
    ret, img = cap.read() 

    hough(img)

    cv2.imshow('image', img)

    # if q is pressed, break
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        cap.release()
        cv2.destroyAllWindows()
        break
