import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from picarx import Picarx


def edge_detection(img):
    # Convert to graycsale
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.bilateralFilter(img,9,75,75)
    img_blur = cv2.GaussianBlur(img_blur, (5,5), 0)
     
    # Sobel Edge Detection
    #sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    #sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image
    linek = np.zeros((11,11), dtype=np.uint8)
    linek[5, ...] = 1
    height, width = edges.shape
    x = 50
    bla = np.zeros((50, 640))
    edges[height-x:height, 0:width] = bla
    #edges -= cv2.morphologyEx(edges, cv2.MORPH_OPEN, linek, iterations=1)
    
    return edges

def lowest_pixel(img):
    img = img[::-1]
    for row in range(0, img.shape[0]):
        for col in range(0, img.shape[1]):
            if (img[row, col] != 0):
                return img.shape[0] - row, img.shape[1] - col

def capture(camera, rawCapture):


    for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
        img = frame.array
        
        edge_image = edge_detection(img)
        cv2.imshow("video", edge_image)  # OpenCV image show
        
        rawCapture.truncate(0)  # Release cache
        return (lowest_pixel(edge_image))


def main():
    px = Picarx()
    with PiCamera() as camera:
        camera.resolution = (640, 480)  
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)
        for angle in range(0,35):
            row, col = capture(camera, rawCapture)
            print (row, col)
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo1_angle(angle)
            row, col = capture(camera, rawCapture)
            print (row, col)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo1_angle(angle)
            row, col = capture(camera, rawCapture)
            print (row, col)

            time.sleep(0.01)



        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close()
    
main()

