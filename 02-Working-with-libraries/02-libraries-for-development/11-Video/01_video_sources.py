import cv2

def display_frames_webcam(save_output):
    cam = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))    

    while True:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        if(save_output):
            out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            out.release()
            break

def display_frames_video():
    # read from video file
    print("TODO")

def display_frames_rtsp():
    # read from rtps stream
    print("TODO")

if __name__ == "__main__":
    display_frames_webcam(True)