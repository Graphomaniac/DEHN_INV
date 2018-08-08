import numpy as np
from scipy.optimize import minimize
import scipy
import time

import cdd
from sympy import Matrix
def Bound_test(A,b):
    norm = lambda x: np.linalg.norm(np.dot(A,x)-b)
    n = A.shape[1]
    solution = minimize(norm, np.zeros(n), method='L-BFGS-B', bounds=[(np.finfo(float).eps,None) for x in xrange(n)])
    if solution['x'].all()>0 and (np.dot(A,solution['x'])-b).all() == 0: 
        return True
    else:
        return False
def Rand_Matrix(m, n, d=0):
    np.random.seed(int(time.clock()*10000))
    return Matrix(np.random.rand(m, n)-d)
def file_mat_output(M, file):
    for i in range(M.shape[0]):
        for s in M[i,:]:
            file.write(str(s)+"\t")
        file.write("\n")
def GRC(base, dim):
    res=[]
    for i in range(dim):
        comb=Rand_Matrix(1, base.shape[0])
        cur_vect=np.zeros(base.shape[1])
        for i in range(comb.shape[1]):
            #print base.shape[0]
            cur_vect=cur_vect+comb[i]*base[i,:]
        res.append(cur_vect)
    res=np.array(res)
    res = np.transpose(res)
    return res
A=Rand_Matrix(1,100)
V=np.array(A.nullspace())
#print V
P=GRC(V, 2)
P=np.hstack((P, np.full((V.shape[1], 1), 1)))
P=cdd.Matrix(P)
P.rep_type=cdd.RepType.INEQUALITY
print P
P=cdd.Polyhedron(P)
res=P.get_generators()
print res
P=np.array(res)
#print hv.compute([1000,0,0])
print P
from scipy.spatial import ConvexHull
hull = ConvexHull(P)
import matplotlib.pyplot as plt
matplotlib.use('Agg')
plt.plot(P[:,0], P[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(P[simplex, 0], P[simplex, 1], 'k-')
