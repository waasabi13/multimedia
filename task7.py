import cv2

video = cv2.VideoCapture(0)


def readIPWriteTOFile():
    # Получаем ширину и высоту видеопотока.
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Задаем кодек для записи видео (в данном случае MP4 с кодеком 'mp4v').
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Создаем объект для записи видео в новый файл "./output/beautiful_user.mp4"
    # с указанным кодеком, частотой кадров 30 кадров в секунду и размерами кадров (w, h).
    video_writer = cv2.VideoWriter("./output/beautiful_user.mp4", fourcc, 30, (w, h))

    while True:
        # Считываем текущий кадр из видеопотока.
        ok, vid = video.read()

        cv2.imshow('Cheese', vid)

        video_writer.write(vid)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Закрываем видеопоток.
    video.release()

    # Закрываем видеопоток записи.
    video_writer.release()

    cv2.destroyAllWindows()

# Вызываем функцию для выполнения операций чтения и записи видео.
readIPWriteTOFile()
