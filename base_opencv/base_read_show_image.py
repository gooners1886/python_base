# coding=utf-8
import cv2
img = cv2.imread("9901_120003.jpg")
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey (0)

i_img_height = img.shape[0]
i_img_width = img.shape[1]
print "i_img_height = {}".format(i_img_height)
print "i_img_width = {}".format(i_img_width)


im_resize = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), None, interpolation=cv2.INTER_LINEAR)
# 保存图片
cv2.imwrite("9901_120003_2.jpg", im_resize)   # 不需要RGB转换!

# 从bgr向rgb转换
# img_rgb = img[:, :, ::-1]