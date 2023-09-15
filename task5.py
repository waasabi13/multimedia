import cv2

img1 = cv2.imread(r'./source/meow1.jpeg')
img2 = cv2.imread(r'./source/meow1.jpeg')

cv2.namedWindow('meow', cv2.WINDOW_NORMAL)
cv2.namedWindow('meow_hsv', cv2.WINDOW_NORMAL)

cv2.imshow('meow',img1)

hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
cv2.imshow('meow_hsv', hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()