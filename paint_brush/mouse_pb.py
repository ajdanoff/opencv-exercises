import cv2
import numpy as np

drawing = False # True if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle a curve.
ix, iy = -1, -1
rad = 0

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, rad

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 1)
            else:
                rad = int(((x-ix)**2 + (y-iy)**2)**0.5)
                cv2.circle(img, (ix, iy), rad, (0, 0, 255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 1)
        else:
            rad = int(((x-ix)**2 + (y-iy)**2)**0.5)
            cv2.circle(img, (ix, iy), rad, (0, 0, 255), 1)


# create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('s'):
        cv2.imwrite('painting.png', img)
    elif k == 27:
        break

cv2.destroyAllWindows()
