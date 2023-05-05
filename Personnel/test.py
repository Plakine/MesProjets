import cv2
import random
from keyboard import on_press_key

img = cv2.imread("C:\\Users\\julie\\Pictures\\map_offrance.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, trash = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(trash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    region = contours[i]
    cv2.drawContours(img, [region], 0, (random.randint(0, 255),
                     random.randint(0, 255), random.randint(0, 255)), -1)
    cv2.imwrite("C:\\Users\\julie\\Pictures\\mapoffrance.png", img)
    while not btnp(KEY_Z):
        pass
cv2.imshow("Colored Map", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
