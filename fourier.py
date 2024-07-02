import numpy as np

def DFT(fk):

    N = len(fk)
    f = []

    for p in range(N):
        fp = 0
        for k in range(N):
            fp += fk[k] * np.exp( -2j * np.pi * p  * k / N)

        f.append(fp)

    return f

def DFT_2(x):
    """
    Function to calculate the
    discrete Fourier Transform
    of a 1D real-valued signal x
    """

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X


def inverseDFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    e = np.exp(2j * np.pi * k * n / N)
    X = np.dot(e,x)

    return np.real(X / N)
dfts = DFT_2([1,2,3,4])

print(dfts)

print(inverseDFT(dfts))
