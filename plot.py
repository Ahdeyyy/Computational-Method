from function import f
from interpolation import linear_spline_interpolation
import matplotlib.pyplot as plt

x = [x for x in range(20)]
y = [f(x) for x in x]
y_hat = linear_spline_interpolation(x,y)
plt.plot(x,y,"-ob")
plt.plot(2.5, y_hat(2.5),"ro")
plt.title("A simple plot")
plt.show()
