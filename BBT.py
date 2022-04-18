import cv2
import apriltag

img = cv2.imread('PXL_20220315_213654374.MP.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
result = th3
out = cv2.resize(result, (result.shape[1]//5,result.shape[0]//5))
cv2.imshow("x",out)
cv2.waitKey()