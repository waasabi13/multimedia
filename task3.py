import cv2

cap = cv2.VideoCapture(r'./source/meow.mp4', cv2.CAP_ANY)

new_width = 640
new_height = 480

while True:
    # Читаем следующий кадр из видеопотока.
    ret, frame = cap.read()
    if not ret:
        exit()
    # Изменяем размер кадра на новые размеры (640x480).
    frame = cv2.resize(frame, (new_width, new_height))  
    # Преобразуем кадр в оттенки серого (градации серого).
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('meow video', gray_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        exit()
