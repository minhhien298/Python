import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100) # từ 0 đến 2, chia ra 100

plt.plot(x, x, label='linear') # hàm bậc nhất
plt.plot(x, x**2, label='quadratic') # hàm bậc hai
plt.plot(x, x**3, label='cubic') # hàm bậc ba
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()