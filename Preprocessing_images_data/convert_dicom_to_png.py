import pydicom
import pylibjpeg
import os
import numpy as np
from PIL import Image
import glob

#get name from folder with path
def get_names(path):
    names = []
    pathOfImages = []
    for filename in glob.glob(os.path.join(path,'*','*.dcm')):
        names.append(filename)
    return names

#convert image dcm to png
def convert_dcm_png(pathOfImage, imageName):
    im = pydicom.dcmread(pathOfImage + '/' + imageName)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)

    return final_image

#main 
if __name__ == '__main__':
    # Nghia: có thể dùng argparse để đưa argument vào main khi chạy python file từ command line
    pathImage = input('Enter the path images: ')
    pathImages = pathImage.rstrip()
    print('pathImages: ====!!!!!', pathImages)
    pathOfEachImages = get_names(pathImages)
    isExist = os.path.exists(pathImages+'/imagePNG')
    if isExist == False:
        os.makedirs(pathImages+'/imagePNG')
    for name in pathOfEachImages:
        head, tail = os.path.split(name)
       #print('pathOfEachImages', pathOfEachImages)
        print('name', name)
        print('head:=========', head)
        print('tail:=========', tail)
        images = convert_dcm_png(head, tail)

        images.save(pathImages+'/imagePNG/' + tail[:-4]+'.png')
    
    print('complete')
        