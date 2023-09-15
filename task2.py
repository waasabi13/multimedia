import cv2

img1 = cv2.imread(r'./source/meow1.jpeg',cv2.IMREAD_GRAYSCALE) #ЧБ
img2 = cv2.imread(r'./source/meow2.png',cv2.IMREAD_UNCHANGED) #без изменений
img3 = cv2.imread(r'./source/meow3.bmp',cv2.IMREAD_ANYDEPTH) # с учетом  глубины цвета
cv2.namedWindow('test1', cv2.WINDOW_NORMAL)
cv2.namedWindow('test2', cv2.WINDOW_NORMAL)
cv2.namedWindow('test3', cv2.WINDOW_NORMAL)
cv2.imshow('test1',img1)
cv2.imshow('test2', img2)
cv2.imshow('test3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
