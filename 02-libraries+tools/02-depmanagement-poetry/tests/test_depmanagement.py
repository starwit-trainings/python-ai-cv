from depmanagement import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_numpy():
    import numpy as np
    arr = np.zeros((2,2))
    assert arr.shape == (2,2)
