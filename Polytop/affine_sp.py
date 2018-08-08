import numpy as np
from sympy import Matrix
from gs_sing import gs
import pycddlib
def eq_to_z(arr):
    for i in arr:
        if abs(i)>=np.finfo(float).eps:
            return False
    return True
def cut_zero_cols(M):
    M=np.transpose(M)
    M=M[~np.all(M == 0, axis=1)]
    return np.transpose(M)
class aff_space():
    def __init__(self, V_Norm, point):
        self.norm=gs(np.transpose(V_Norm))
        self.norm=cut_zero_cols(self.norm)
        self.OR=point
        self.basis=gs((np.transpose(np.concatenate((np.transpose(self.norm), np.identity(self.norm.shape[0]))))))
        self.basis=cut_zero_cols(self.basis[:,self.norm.shape[1]:])
    def proj(self, vector):
        res=[]
        for i in np.transpose(self.basis):
            res.append(np.dot(vector, i))
        return np.array(res)
    def proj_pt(self, point):
        return self.proj(point-self.OR)
    def printf(self):
        print(self.basis)
space=aff_space(np.array([[1.,1.,0.], [-1, -1, 1]]), np.array([0., 0., 0.]))
space.printf()
print (space.proj([1.,0., 0]))
print (space.proj_pt([0.,21.,0.]))