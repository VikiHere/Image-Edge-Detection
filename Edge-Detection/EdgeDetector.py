import numpy as np
from PIL import Image
import math

from derivative_kernel import derivative_kernel
from spatial_filter import spatial_filter
from spatial_filter import chkOv
from  non_max_suppress import non_max_suppress
from image_threshold import image_threshold

        
def edge_detector(img, H, T, wndsz):

#Part 1 : Veritcal and Horizontal Gradients

    vimg = img
    himg = img

    col, row = img.shape

    kernelv = derivative_kernel(4)
    kernelh = np.transpose(derivative_kernel(4))

    vout_img = spatial_filter(vimg, kernelv)
    hout_img = spatial_filter(himg, kernelh)


#Part 2 : Gradient Magnitude
    gradMag = np.zeros(shape=img.shape)#img

    for x in range (gradMag.shape[0]):
        for y in range (gradMag.shape[1]):
            gradMag[x][y] = math.sqrt((vout_img[x][y]**2) + (hout_img[x][y]**2))

    temp = gradMag

#Part 3 : Non-Maximum Surpression 
    #Split the Gradient Magnitude into vertical and horizontal
    tempv = gradMag
    temph = gradMag

    #NMS the two
    vnms = non_max_suppress(gradMag, 1, wndsz)
    hnms = non_max_suppress(gradMag, wndsz, 1)

#Part 4 : Threshold

    #Applying Threshold to the 2 images
    vthreshold = image_threshold(vnms, T)
    hthreshold = image_threshold(hnms, T)

    #combining the images
    combthreshold = vthreshold

    for x in range (vthreshold.shape[0]):
        for y in range (vthreshold.shape[1]):
            combthreshold[x][y] = (vthreshold[x][y] or hthreshold[x][y])

    combthresholdImg = Image.fromarray(chkOv(combthreshold.astype('uint8')), mode='L')
    combthresholdImg.save("Centural.png")


if __name__== "__main__":
    
#Ask for imputs
    imgInput = input("Please type out the image name (including extension) ")
    H = int(input("Input the kernel ")) 
    t = input("Optional: input Threshold value " )
    wdsz = input("Optional: input size of NMS filter ")

    img = np.asarray(Image.open(imgInput).convert('L'), dtype='float')

#appropriate types casting
    kernelArr = derivative_kernel(H)    

    if (t == "" and wdsz == ""):
        T = 0.1
        wndsz = 5
    elif (t == ""):
        T = 0.1
    elif (wdsz == ""):
        wndsz = 5
    else:
        T = float(t)
        wndsz = int(wdsz)

    edge_detector(img, kernelArr, T, wndsz)

