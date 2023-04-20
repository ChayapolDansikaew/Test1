import numpy as np

def f3(M, v):
    #M : 2-D numpy array
    #v : 1-D numpy array
    #note : v.shape[0] equals to M.shape[1]
    A = []
    for i in range(M.shape[0]):
        a = []
        for j in range(M.shape[0]):
            a.append(M[i,j] * v[j])
        A.append(a)
    return np.array(A)
