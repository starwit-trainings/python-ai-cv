import cv2

def display_frames_webcam():
    cam = cv2.VideoCapture(0)

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
    cv2.namedWindow('webcam', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('webcam', 1280, 720)

    while True:
        ret, frame = cam.read()
        frame = manipulate_video("draw", frame)
        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            out.release()
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
    return frame

def find_edges(frame):
    # TODO
    return frame

if __name__ == "__main__":
    positionX = 10;
    positionY = 10;
    display_frames_webcam()