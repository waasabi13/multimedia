import cv2
import numpy as np

# Открываем видеопоток с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Считываем кадр из видеопотока
    ret, frame = cap.read()
    if not ret:
        break

    # Получаем высоту, ширину и количество каналов изображения.
    height, width, _ = frame.shape

    # Создаем пустое изображение с такими же размерами
    cross_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Определяем параметры для вертикальной линии
    vertical_line_width = 60
    vertical_line_height = 300

    # Рисуем вертикальную линию на пустом изображении
    cv2.rectangle(cross_image,
                  (width // 2 - vertical_line_width // 2, height // 2 - vertical_line_height // 2),
                  (width // 2 + vertical_line_width // 2, height // 2 + vertical_line_height // 2),
                  (0, 0, 255), 2)

    # Определяем параметры для горизонтальной линии
    horizontal_line_width = 250
    horizontal_line_height = 55

    # Рисуем горизонтальную линию на пустом изображении
    cv2.rectangle(cross_image,
                  (width // 2 - horizontal_line_width // 2, height // 2 - horizontal_line_height // 2),
                  (width // 2 + horizontal_line_width // 2, height // 2 + horizontal_line_height // 2),
                  (0, 0, 255), 2)

    # Объединяем оригинальное изображение с изображением с крестиками с помощью взвешенной суммы
    result_frame = cv2.addWeighted(frame, 1, cross_image, 0.5, 0)


    cv2.imshow("За вами не следит скрытая камера", result_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы закрывая видеопоток
cap.release()


cv2.destroyAllWindows()
