# Nghia: tránh việc đặt tên file bằng tiếng Việt (vd: "am_ban")

import cv2
import glob
import os
dem=0 # Nghia: tránh việc đặt tên biến tiếng Việt
for f in glob.glob(r"D:\Breast_Cancer_Detection\train_val\train\*.png"):
    # image=cv2.imread(f)
    image = cv2.imread(f) # Nghia: nên có dấu cách trước và sau dấu bằng
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image=cv2.resize(image,(300,300))
    am_ban = 255 - image # Nghia: tránh việc đặt tên biến tiếng Việt
    # cv2.imwrite(f,am_ban) # Nghia: dấu cách sau dấu phẩy
    cv2.imwrite(f, am_ban) 
    # dem+=1
    dem += 1 # Nghia: dấu cách trước và sau dấu + - * / = %
    print(dem)