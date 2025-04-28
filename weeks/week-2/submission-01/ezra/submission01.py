import cv2
import numpy as np

def draw(event, x, y, flags, param):
    global canvas, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas, (320, 100), 30, (255, 0, 0), 2)
        cv2.rectangle(canvas, (290, 130), (350, 230), (0, 255, 0), 2)
        cv2.line(canvas, (290, 150), (250, 200), (0, 0, 255), 3)
        cv2.line(canvas, (350, 150), (390, 200), (0, 0, 255), 3)
        cv2.line(canvas, (300, 230), (270, 300), (0, 0, 255), 3)
        cv2.line(canvas, (340, 230), (370, 300), (0, 0, 255), 3)
        cv2.putText(canvas, 'GondrongMan', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw)

while True:
    cv2.imshow('Canvas', canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
