import cv2
import glob
import os
dem=0
for f in glob.glob(r"D:\Breast_Cancer_Detection\train_images\imgPNG3\*.png"):
    image=cv2.imread(f)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image=cv2.resize(image,(300,300))
    cv2.imwrite(f,image)
    dem+=1
    print(dem)
