# How to setup Mediamtx RTSP server

For network video streaming we use Mediamtx to turn USB cams or videos feeds to RTSP sever. Tool can be downloaded here: https://github.com/bluenviron/mediamtx

## Linux
* Install ffmpeg, Ubuntu: sudo apt install ffmpeg
* list USB cams: v4l2-ctl --list-devices
* sample config file
    ```yml
    paths:
    cam:
        runOnInit: ffmpeg -f v4l2 -i /dev/video0 -pix_fmt yuv420p -preset ultrafast -b:v 600k -f rtsp rtsp://localhost:$RTSP_PORT/$MTX_PATH
        runOnInitRestart: yes
    ```

## Windows
* Install ffmpeg
* Open Powershell
    ```
    winget install "FFmpeg (Essentials Build)"
    ```
* restart shell to get binaries to path
* List USB cams: ffmpeg -list_devices true -f dshow -i dummy
* sample config file
    ```yml
    paths:
    cam:
        runOnInit: ffmpeg -f dshow -i video="USB 2.0 Camera " -pix_fmt yuv420p -c:v libx264 -preset ultrafast -b:v 600k -f rtsp rtsp://localhost:$RTSP_PORT/$MTX_PATH
        runOnInitRestart: yes
    ```

## Common Usage
* Test if sever is working: ffplay rtsp://localhost:8554/cam