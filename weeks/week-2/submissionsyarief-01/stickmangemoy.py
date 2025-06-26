import cv2 as cv
import numpy as np
import os

print("OpenCV version: ", cv.__version__)
print("Current Working Directory:", os.getcwd())

canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

drawing = False
mode = 'circle'
ix, iy = -1, -1

cv.putText(canvas, 'Si Gondrong', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            temp_canvas = canvas.copy()
            if mode == 'circle':
                cv.circle(temp_canvas, (ix, iy), int(np.hypot(x-ix, y-iy)), (0, 0, 255), 2)
            elif mode == 'rectangle':
                cv.rectangle(temp_canvas, (ix, iy), (x, y), (0, 255, 0), 2)
            elif mode == 'line':
                cv.line(temp_canvas, (ix, iy), (x, y), (255, 0, 0), 3)
            cv.imshow('Stickman Drawing', temp_canvas)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'circle':
            cv.circle(canvas, (ix, iy), int(np.hypot(x-ix, y-iy)), (0, 0, 255), 2)
        elif mode == 'rectangle':
            cv.rectangle(canvas, (ix, iy), (x, y), (0, 255, 0), 2)
        elif mode == 'line':
            cv.line(canvas, (ix, iy), (x, y), (255, 0, 0), 3)

cv.namedWindow('Stickman Drawing')
cv.setMouseCallback('Stickman Drawing', draw)

print("""
[INSTRUKSI]:
- Tekan 'c' untuk mode lingkaran (kepala)
- Tekan 'r' untuk mode persegi (badan)
- Tekan 'l' untuk mode garis (organ)
- Tekan 'q' untuk keluar
""")

while True:
    cv.imshow('Stickman Drawing', canvas)
    k = cv.waitKey(1) & 0xFF

    if k == ord('c'):
        mode = 'circle'
    elif k == ord('r'):
        mode = 'rectangle'
    elif k == ord('l'):
        mode = 'line'
    elif k == ord('q'):
        break

cv.destroyAllWindows()
