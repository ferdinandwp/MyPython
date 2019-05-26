import numpy as np
import matplotlib.pyplot as plt

#define arrays
linear = np.arange(1,20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(1,100,20)


#plot
plt.plot(linear)
plt.plot(square)
plt.plot(log)
plt.plot(random)

plt.show()
plt.close()








