import time
import cv2
def rtspCamera():
    rtsp_str = 'http://admin:admin@192.168.1.20:8081/video'
    video = cv2.VideoCapture(rtsp_str)
    while True:
        ok, img = video.read()
        if ok:
            cv2.imshow('wow', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
rtspCamera()