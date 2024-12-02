import cv2
import numpy as np

def display_frames_webcam():
    cam = cv2.VideoCapture(2)

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    cv2.namedWindow('webcam', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('webcam', 1280, 720)

    while True:
        ret, frame = cam.read()
        frame = manipulate_video("corner", frame)
        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break

def manipulate_video(mode, frame):
    match mode:
        case "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        case "draw":
            global positionX, positionY

            if(positionX < 1280):
                positionX += 1
            else:
                positionX = 10
            frame = cv2.rectangle(frame, (positionX, positionY), (positionX + 200, positionY + 200), (0, 0, 0), -1)
        case "blur":
            frame = cv2.blur(frame, (5, 5))
        case "edges":
            frame = find_edges(frame)
        case "corner":
            frame = find_corners(frame)
    return frame

def find_edges(frame):
    # TODO
    return frame

def find_corners(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(frame, 3, 5, 0.1)
    corners = dst > 0.05 * dst.max()
    coord = np.argwhere(corners)
    for y, x in coord:
        cv2.circle(frame, (x,y), 3, (0,0,255), -1)    
    return frame

if __name__ == "__main__":
    positionX = 10;
    positionY = 10;
    display_frames_webcam()