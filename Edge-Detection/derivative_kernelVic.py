import numpy as np
from PIL import Image

def derivative_kernel(x):
    """
        Pass in a integer from 1 - 4
            1 - Centural Difference 
            2 - Forward Difference
            3 - Prewitt
            4 - Sobel
    """

    centural = {[1 0 -1]}
    forward = {[0 1 -1]}
    prewitt = {[1 0 -1], [1 0 -1]], [1 0 -1]]}
    sobel = {[1 0 -1], [2 0 -2], [1 0 -1]}