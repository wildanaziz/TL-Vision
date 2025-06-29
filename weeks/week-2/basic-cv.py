import cv2 as cv
import numpy as np
import os

print("OpenCV version: ", cv.__version__)

print(os.getcwd())

# # load image 1
img1 = cv.imread('../../assets/img/sample-images-main/images/image-2.jpg')
cv.imshow('Image 1', img1)

# load video
cap = cv.VideoCapture('../../assets/videos/drummer.mp4')

#load live video webcam
capWebcam = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()

    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

    isTrueWebcam, frameWebcam = capWebcam.read()

    cv.imshow('Webcam Video', frameWebcam)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
capWebcam.release()
cv.destroyAllWindows()
cv.waitKey(0)

# make a function for resize image, video and webcam
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resize image 1
img1_resized = rescaleFrame(img1, scale=0.5)
cv.imshow('Image 1 Resized', img1_resized)

# resize video
capResizeVideo = cv.VideoCapture('../../assets/videos/drummer.mp4')
capResizeWebcam = cv.VideoCapture(0)

while True:
    isTrue, frame = capResizeVideo.read()

    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# resize webcam
    isTrueWebcam, frameWebcam = capResizeWebcam.read()

    frameWebcam_resized = rescaleFrame(frameWebcam, scale=0.5)

    cv.imshow('Webcam Video Resized', frameWebcam_resized)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capResizeVideo.release()
capResizeWebcam.release()
cv.destroyAllWindows()

# function for change resolution
def changeRes(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10, 200)  # brightness
    return cap

# change resolution of webcam
capChangeResWebcam = cv.VideoCapture(0)
capChangeResWebcam = changeRes(capChangeResWebcam, 1366, 768)

while True:
    isTrueWebcam, frameWebcam = capChangeResWebcam.read()

    cv.imshow('Webcam Video Resized', frameWebcam)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capChangeResWebcam.release()
cv.destroyAllWindows()

# draw anything on blank canvas
blank  = np.zeros((512, 512, 3), dtype=np.uint8)
cv.imshow('Blank', blank)

# draw a rectangle & circle
cv.rectangle(blank, (150, 100), (460, 400), (0, 255, 0), thickness=2)
cv.circle(blank, (250, 250), 40, (255, 0, 0), thickness=-1)
cv.line(blank, (155, 105), (250, 250), (0, 0, 255), thickness=3)
cv.imshow('Rectangle & Circle', blank)

# draw text
cv.putText(blank, 'TL-Vision OpenCV', (140, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)

# draw with mouse
drawing = False
mode = True

ix, iy = 0, 0

def draw_circle(event, x, y, flags, params):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(new_blank_canvas, (ix, iy), (x, y), (0, 0, 255), 1)
            else:
                cv.circle(new_blank_canvas, (x, y), 10, (0, 255, 0), -1)
    
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(new_blank_canvas, (ix, iy), (x, y), (0, 0, 255), 1)
        else:
            cv.circle(new_blank_canvas, (x, y), 10, (0, 255, 0), -1)

new_blank_canvas = np.zeros((512, 512, 3), dtype=np.uint8)

while True:
    cv.imshow('Draw on Blank Canvas', new_blank_canvas)
    cv.setMouseCallback('Draw on Blank Canvas', draw_circle)
    chmod = cv.waitKey(1) & 0xFF
    if chmod == ord('m'):
        mode = not mode
    elif chmod == 27:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

# image transformation

# translation
def transMat(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y], [0,0,1]])
    dimensions = img.shape[1], img.shape[0]
    translated_img = cv.warpPerspective(img, transMat, dimensions)

    return translated_img

# load image for translation
img2 = cv.imread('../../assets/img/sample-images-main/images/image-3.jpg')
img2 = transMat(img2, 100, 100)
cv.imshow('Translated Image', img2)

# rotation
def rotateMat(img, angle, rotatePoint=None):
    if rotatePoint is None:
        rotatePoint = (img.shape[1] // 2, img.shape[0] // 2)
    
    rotateMat = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    dimensions = img.shape[1], img.shape[0]
    rotated_img = cv.warpAffine(img, rotateMat, dimensions)

    return rotated_img

# load image for rotation
img3 = cv.imread('../../assets/img/sample-images-main/images/image-3.jpg')
img3 = rotateMat(img3, 45)
cv.imshow('Rotated Image', img3)

# resize
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# load image for resize
img3 = cv.imread('../../assets/img/sample-images-main/images/image-3.jpg')
img3_resized = rescaleFrame(img3, 0.5)
cv.imshow('Resized Image', img3_resized)

# flip
def flipMat(img, flipCode):
    flipped_img = cv.flip(img, flipCode)

    return flipped_img

# load image for flip
img3 = cv.imread('../../assets/img/sample-images-main/images/image-3.jpg')
img3_flipped = flipMat(img3, 1)
cv.imshow('Flipped Image', img3_flipped)

# crop
def cropMat(img, x, y, w, h):
    cropped_img = img[y:y+h, x:x+w]

    return cropped_img
# load image for crop

img3 = cv.imread('../../assets/img/sample-images-main/images/image-3.jpg')
img3_cropped = cropMat(img3, 100, 100, 300, 300)
cv.imshow('Cropped Image', img3_cropped)
cv.waitKey(0)

# contours

img5 = cv.imread('../../assets/img/sample-images-main/images/image-5.jpg')
img5_gray = cv.cvtColor(img5, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', img5_gray)

# canny edge detection
img5_canny = cv.Canny(img5_gray, 100, 200)
cv.imshow('Canny Edge Detection', img5_canny)

# find contours
contours, hierarchy = cv.findContours(img5_canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print('Number of contours found canny: ', len(contours))

# threshold
ret, threshold = cv.threshold(img5_gray, 127, 255, cv.THRESH_BINARY)
cv.imshow('Threshold Image', threshold)
# find contours
contours, hierarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print('Number of contours found thresh: ', len(contours))

# blur
img5_blur = cv.GaussianBlur(img5_gray, (5, 5), 0)
cv.imshow('Blurred Image', img5_blur)

# draw contours
cv.drawContours(img5_blur, contours, -1, (0, 0, 255), 2)
cv.imshow('Draw Contours', img5_blur)

# average blurr
average = cv.blur(img5_blur, (5, 5))
cv.imshow('Average Blurr', average)

# median blurr
median = cv.medianBLur(img5_blur, (5, 5))
cv.imshow('Median Blurr', median)

# bilateral blur
bilateral = cv.bilateralFilter(img5_blur, 9, 75, 75)
cv.imshow('Bilateral Blurr', bilateral)

cv.waitKey(0)

# mini project - face detection

import cv2 as cv

cv.imshow('Group of 5 people', img1)

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img1, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img1)

cv.waitKey(0)

# mini project - face detection with webcam
video = cv.VideoCapture(0)  

# Load Haar cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = video.read()
    if not isTrue:
        print("Video tidak dapat dibaca atau sudah selesai.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
    print(f'Number of faces found = {len(faces_rect)}')

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Faces', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
