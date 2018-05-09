import cv2
import numpy

img = numpy.zeros((100,100,3),dtype='uint8')

img[:,:,0] = numpy.ones((100,100))*255
# img[:,:,1] = numpy.ones((10,10))*128/255.0
# img[:,:,2] = numpy.ones((10,10))*192/255.0

# cv2.imwrite('color_img.jpg', img)
# img = cv2.imread("images/test_rgb_3.png")
cv2.imshow("images/test_rgb_3.png", img);
cv2.waitKey();