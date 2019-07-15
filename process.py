import glob
import cv2 as cv
import os

img_list=glob.glob("*.bmp")
dirs = 'new'
if not os.path.exists(dirs):
    os.makedirs(dirs)
for i in range(len(img_list)):
    img=cv.imread(img_list[i])
    img_name=os.path.splitext(img_list[i])[0]
    ext=os.path.splitext(img_list[i])[1]
    cv.imwrite("./new/"+img_name+'_rgb_base'+ext,img)

