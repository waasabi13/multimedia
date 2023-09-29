import cv2


def readIPWriteTOFile():
    video = cv2.VideoCapture(r'./source/meow.mp4', cv2.CAP_ANY)

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Задаем кодек для записи видео (в данном случае MP4 с кодеком 'mp4v').
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Создаем объект для записи видео в новый файл './output/output_meow.mp4'
    # с указанным кодеком, частотой кадров 25 кадров в секунду и размерами кадров (w, h).
    video_writer = cv2.VideoWriter("./output/output_meow.mp4", fourcc, 25, (w, h))

    # Закрываем видеопоток чтения.
    video.release()

    # Закрываем видеопоток записи.
    video_writer.release()

    cv2.destroyAllWindows()

readIPWriteTOFile()
