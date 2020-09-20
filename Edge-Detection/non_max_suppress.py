'''
NMS (Non Maximum Suppression)

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    print("Format: python non_max_suppress.py *image* *window height* *window width*")
    imgName = input("Please enter image name: ")
    winHeight = input("Please enter window height: ")
    winWidth = input("Please enter window width: ")                   
        
    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint32')
    out = non_max_suppress(img, (int)(winHeight), (int)(winWidth)).astype('uint8')
 
    final = Image.fromarray(out)
    final.show()
    final.save("nms_5by5.png")

# Non Maximum Suppresion
def non_max_suppress(img, H, W):

    padX = (int)(H/2)
    padY = (int)(W/2)
    print("PadX = ", padX)
    print("PadY=", padY)
    # creating padded Image
    temp = np.zeros(shape=(2*padX + img.shape[0], 2*padY + img.shape[1]))
    temp[padX : img.shape[0] + padX, padY : img.shape[1] + padY] = img

    #final image
    out_img = img

    # sliding the window accross the image
    for row in range(padX, img.shape[0]+padX):       # row
       for col in range(padY, img.shape[1]+padY):   # column
            startX = row - padX
            startY = col - padY
            endX = startX + H
            endY = startY + W
            window = temp[startX : endX, startY : endY]
            currElement =  temp[row][col]

            if (currElement < np.amax(window)):
                out_img[row - padX][col - padY] = 0
    
    print(out_img)
    return out_img

if __name__ == '__main__':
    main()