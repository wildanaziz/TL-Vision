import cv2 as cv
import numpy as np
import os

print("OpenCV version: ", cv.__version__)

print(os.getcwd())

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
            temp = new_blank_canvas.copy() #kenapa harus copy?kita mencetak canvas baru agar tidak mengganggu canvas utama
            if mode == True:
                cv.rectangle(temp, (ix, iy), (x, y), (0, 0, 255), 1, 8)
            else:
                cv.circle(temp, (x, y), 10, (0, 255, 0), -1)
            # cv.imshow('Draw on blank canvas', temp) ## ini adalah sebuah blank canvas untuk menggambar dari cursor
            ## pada canvas copy kita dapat melihat gambar kota yang diarahkan oleh kursor
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
