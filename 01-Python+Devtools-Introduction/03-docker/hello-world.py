import time
import numpy as np

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

i = 1
while True:
    print("Hello World")
    time.sleep(3)

    divisible = array_example[array_example%i==0]
    print(divisible)
    if i == 10:
        i = 1
    else:
        i += 1
