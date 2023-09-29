import cv2

img1 = cv2.imread(r'./source/meow1.jpeg')
img2 = cv2.imread(r'./source/meow1.jpeg')

# Создаем окна для отображения изображений с именами 'meow' и 'meow_hsv'.
cv2.namedWindow('meow', cv2.WINDOW_NORMAL)
cv2.namedWindow('meow_hsv', cv2.WINDOW_NORMAL)

# Отображаем изображение img1 в окне 'meow'.
cv2.imshow('meow', img1)

# Преобразуем изображение img2 из цветового пространства BGR в цветовое пространство HSV.
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Отображаем изображение hsv (в цветовом пространстве HSV) в окне 'meow_hsv'.
cv2.imshow('meow_hsv', hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()
