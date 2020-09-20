import numpy as np

def derivative_kernel(input):
    """ 'derivative_kernel(x)': provides a kernel matrix 'y' based on passed paramater 'x'
    input:
        - int 'x': ranges '1' to '4'; used to select which kernel to return
    output:
        - numpy.array 'y': numpy matrix of corresponding kernel; possible return values:
                x = 1: Central Difference Kernel (1x3 matrix)
                x = 2: Forward Difference Kernel (1x3 matrix)
                x = 3: Prewitt Kernel (3x3 matrix)
                x = 4: Sobel Kernel (3x3 matrix)
                else:   INVALID, returns null
    requires:
        - NumPy library
    """
    if (input == 1):        # Central Difference kernel
        return np.array([1, 0, -1]).reshape(1, 3)
    elif (input == 2):      # Forward Difference kernel
        return np.array([1, 0, -1]).reshape(1, 3)
    elif (input == 3):      # Prewitt kernel
        return np.array([   [1, 0, -1],
                            [1, 0, -1],
                            [1, 0, -1]])
    elif (input == 4):      # Sobel kernel
        return np.array([   [1, 0, -1],
                            [2, 0, -2],
                            [1, 0, -1]])
    else:
        print("Invalid input! Enter number 1 - 4")
        return
