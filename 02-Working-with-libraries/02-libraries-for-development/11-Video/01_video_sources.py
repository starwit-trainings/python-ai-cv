import cv2

def display_frames_webcam():
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break

def display_frames_video():
    # read from video file
    print("TODO")

def display_frames_rtsp():
    # read from rtps stream
    print("TODO")

if __name__ == "__main__":
    display_frames_webcam()