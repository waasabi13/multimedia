import cv2

video = cv2.VideoCapture(0)

def readIPWriteTOFile():

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("./output/beautiful_user.mp4", fourcc, 30, (w, h))

    while (True):
        ok, vid = video.read()

        cv2.imshow('Cheese', vid)
        video_writer.write(vid)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()

readIPWriteTOFile()