import cv2
print('Reading images from different source')

def read_image(image_path):
    img = cv2.imread(image_path)
    cv2.imshow('Outout', img)
    cv2.waitKey(20)

def read_video(video_path):
    capture_video = cv2.VideoCapture(video_path)
    while True:
        status, img = capture_video.read()
        cv2.imshow('Video', img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
           break;

def read_webcam():
    print('Webcam read is in progress')
    capture_video = cv2.VideoCapture(0)
    capture_video.set(3,640) # Width
    capture_video.set(4,480) # Height
    #capture_video.set(10,1) # Brightness
    while True:
        success, img = capture_video.read()
        cv2.imshow('Video', img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
           break;


read_image('Resources/lena.png')
#read_video('Resources/testVideo.mp4')
read_webcam()