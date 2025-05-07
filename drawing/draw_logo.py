import numpy as np
import cv2


# create a black image
img = np.zeros((512, 512, 3), np.uint8)
backgr_color = (237, 149, 100)
cv2.rectangle(img, (0, 0), (512, 512), backgr_color, -1)

######################
#
#         # (256, 201)
#        # # (256,256)
#       #   ######
#      #     #  #
#     #########
#        128
#
######################

triangle_center = (256, 256)
triangle_height = 111
rad = int(triangle_height/2)
circle_thikness = rad - 30
half_height_width = 64
triangle_poly = [
    [triangle_center[0], triangle_center[1] - rad],
    [triangle_center[0] - half_height_width, triangle_center[1] + rad],
    [triangle_center[0] + half_height_width, triangle_center[1] + rad]
    ]

triangle_poly_half = [
    [triangle_center[0] + int(half_height_width/2), triangle_center[1]],
    [triangle_center[0] + int(1.5*half_height_width), triangle_center[1]],
    [triangle_center[0] + half_height_width, triangle_center[1] + rad]
    ]

# red circle
circle_rad = rad - 10 - int(circle_thikness/2)
cv2.circle(img, (triangle_center[0], triangle_center[1] - rad), circle_rad, (0,0,255), circle_thikness)

# green circle
cv2.circle(img, (triangle_center[0] - rad, triangle_center[1] + rad), circle_rad, (0,255,0), circle_thikness)

pts = np.array(triangle_poly, np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (255,255,255))
cv2.fillPoly(img, [pts], backgr_color)

# blue circle
cv2.circle(img, (triangle_center[0] + half_height_width, triangle_center[1] + rad), circle_rad, (255,0,0), circle_thikness)

# half triangle
pts_half = np.array(triangle_poly_half, np.int32)
cv2.fillPoly(img, [pts_half], backgr_color)

# text
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 5
font_scale = 2
cv2.putText(
    img,
    'OpenCV',
    (triangle_center[0] - half_height_width - 2*circle_thikness, triangle_center[1] + 2*rad + 2*circle_thikness),
    font,
    font_scale,
    (255, 255, 255),
    font_size,
    cv2.LINE_AA
)

cv2.namedWindow('drawing', cv2.WINDOW_NORMAL)
cv2.imshow('drawing', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
