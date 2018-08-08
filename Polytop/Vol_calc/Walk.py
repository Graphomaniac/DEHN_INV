import numpy as np
from Pol import *
def dot_product(v1, v2):
    if(v1.shape[0]!=v2.shape[0]):
        return 0
    res=0.
    for i in range(v1.shape[0]):
        res+=v1[i]*v2[i]
    return res
def Vect(p):
    vector=np.random.rand(p.shape[0])
    res=np.array(vector)
    return res/np.linalg.norm(res)
def ORPL(p, P, vect):#procedure to Obtain Random Point on Line
    #print vect
    #print np.array(P.A[0])
    for i in (np.dot(P.A, p)+P.B):
        #print i
        if i<0:
            return None
    MU=([(-P.B[i]+dot_product(P.A[i],p))/dot_product(P.A[i], vect)  for i in range(P.num)])
    MU=sorted(MU, key = lambda x: abs(x))
    mu1=MU[0]
    #print MU
    inside=0
    for i in MU:
        if(i*mu1<=0):
            inside=1
            mu2=i
    if(inside==0):
        mu2=MU.pop()
    res=np.random.uniform(mu1, mu2)
    return res
def Walk(p, P, W):
    for i in range(W):
        l=Vect(p)
        tmp=ORPL(p, P, l)
        if(tmp!=None):
            p=p+l*tmp
        else:
            return None
    return p
P=Polyhedron(np.transpose(np.array([np.array([-7.05764844283602,1,0]),np.array([-21.7631919299345,0,1])])), np.array([1, 1, 1]))
print Walk(np.array([0, 0]), P, 1)