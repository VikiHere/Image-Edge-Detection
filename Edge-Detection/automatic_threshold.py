import numpy as np

def automatic_threshold(gm):
    
    # Kernel size
    H = 3
    W = 3
    
    # Padding sizes
    padX = (int)(H/2)
    padY = (int)(W/2)

    # creating padded Image
    temp = np.zeros(shape=(2*padX + gm.shape[0], 2*padY + gm.shape[1]))
    temp[padX : img.shape[0] + padX, padY : img.shape[1] + padY] = gm

    #final image
    out_img = gm

    # List of max values from every filter
    lst = np.empty(1, dtype='float')

    # sliding the window accross the image
    for row in range(padX, gm.shape[0]+padX):       # row
       for col in range(padY, gm.shape[1]+padY):   # column
            startX = row - padX
            startY = col - padY
            endX = startX + H
            endY = startY + W
            window = temp[startX : endX, startY : endY]
            lst.append(np.amax(window))

    # Get median of the list and return it as the threshold value
    return lst.median()