import numpy as np
from scipy import stats
def S_sq(arr1, arr2):
    return np.sqrt(1/float(len(arr1))+1/float(len(arr2)))*np.sqrt(((((arr1-arr1.mean())**2).sum()+(arr2-arr2.mean())**2).sum()))/np.sqrt(len(arr1)+len(arr2)-2)
def solve_35():
    X = np.array([1.78, 1.81, 1.94, 1.86, 2.00])
    Y = np.array([0.92, 0.78, 0.89, 0.82, 0.92])
    gamma=0.95
    n1=len(X)
    n2=len(Y)
    St_Dist=stats.t(len(X)+len(Y)-2)
    S_qs=S_sq(X,Y)
    g1=X.mean() - (Y.mean()-1) - St_Dist.ppf(1-(1-gamma)/2)*S_qs
    g2=X.mean() - (Y.mean()-1) - St_Dist.ppf(1-(1+gamma)/2)*S_qs
    print("task 35", '{0:.16f}'.format(g1), '{0:.16f}'.format(g2))
    #print(np.sqrt((1/n1+1/n2)*(((X-X.mean())**2).sum()+((Y-Y.mean())**2).sum())/(n1+n2-1)),
    #St_Dist.ppf((1+gamma)/2))
    """print('{0:.16f}'.format(S_qs))
    print(1/n1, np.sqrt(n1+n2-2))"""
solve_35()
def solve_44():
  file=open("input_data.dat", 'r+')
  lines = file.readlines()
  lines=[l.strip() for l in lines]
  #print(lines)
  for i in range(len(lines)):
      #print(lines[i])
      if lines[i]=='Data for task 44': 
        break
  X=[float(x) for x in lines[i+1].split(' ')]
  X=np.array(X)
  Y=np.array([float(x) for x in lines[i+2].split(' ')])
  n1=len(X)
  n2=len(Y)
  Chi_d=stats.chi2(n1-1)
  gamma=0.05
  g2=np.sqrt(((X-X.mean())**2).sum()/Chi_d.ppf(gamma/2))
  g1=np.sqrt(((X-X.mean())**2).sum()/Chi_d.ppf(1-gamma/2))
  print(g1, g2)
  g2=np.sqrt(((Y-Y.mean())**2).sum()/Chi_d.ppf(gamma/2))
  g1=np.sqrt(((Y-Y.mean())**2).sum()/Chi_d.ppf(1-gamma/2))
  print(g1, g2)
  file.close()
print("task 44")
solve_44()
def determine_bounds(quantile, Distr):
    MAX=Distr.ppf(1-3*quantile/4)-Distr.ppf(quantile/4)
    RES=[Distr.ppf(quantile/4), Distr.ppf(1-quantile/4)]
    for i in range(3000):
        d1=Distr.ppf(quantile/4+i*quantile/4000)
        d2=Distr.ppf(1-quantile+(quantile/4+i*quantile/4000))
        if d2-d1<MAX:
            MAX=d2-d1
            RES=[d1, d2]
    return [MAX]+RES
print(determine_bounds(0.05, stats.chi2(0.5)))
def solve_class():
    X = np.array([1.78, 1.81, 1.94, 1.86, 2.00])
    Y = np.array([1.92, 1.78, 1.89, 1.82, 1.92])
    T=(X.mean()-Y.mean())/S_sq(X,Y)
    st=stats.t(len(X)+len(Y)-2)
    if(st.ppf(0.025)<2*T<st.ppf(1-0.025)):
        print("Fits")
    else:
        print("Declined")
    print(2*T)
solve_class()
        