import numpy as np
from scipy import stats
def solve_35():
  X = np.array([1.78, 1.81, 1.94, 1.86, 2.00])
  Y = np.array([0.92, 0.78, 0.89, 0.82, 0.92])

  n_1 = len(X)
  n_2 = len(Y)

  sub_from = X.mean() - Y.mean() + 1
  divide_by = np.sqrt((1/float(n_1)+1/float(n_2))*(((X - X.mean()) ** 2).sum() + ((Y - Y.mean()) **2).sum())/np.sqrt(n_1+n_2-2))

  degrees = n_1 + n_2 - 2
  Chi_d = stats.t(degrees)

  # (sub_from - m) / div ~ St(n)

  def get_bound(quantile):
     return sub_from - Chi_d.ppf(1 - quantile) * divide_by

  gamma = 0.95
  print(get_bound((1 - gamma) / 2), get_bound((1 + gamma) / 2))

solve_35()