# some examples for importing libraries

import numpy as np
import pprint as pp

values = {
        "sampleNumber": 114,
        "subjects": [
            {"id":'A',"temp": 37.4, "height": 174, "gender": 'male'},
            {"id":'B',"temp": 36.6, "height": 154, "gender": 'female'},
            {"id":'C',"temp": 37.0, "height": 170, "gender": 'male'}
            ]
        }

print(values)
pp.pprint(values)

a = np.array([[1, 0, 0, 0], 
              [0, 1, 0, 0], 
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
print(a)
pp.pprint(a)