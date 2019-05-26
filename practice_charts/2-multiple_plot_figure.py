import os
import numpy as np
import matplotlib.pyplot as plt

linear = np.arange(1, 20)
square = linear ** 2
log = np.log(linear)
random = np.random.randint(0, 100, 20)

fig, axes = plt.subplots(2,2,figsize=(10,10))

axes[0][0].plot(linear)
axes[0][1].plot(square)
axes[1][0].plot(log)
axes[1][1].plot(random)

#allow matplotlib to space each figures automatically
plt.tight_layout()

#make folder to store figure
os.makedirs('plots', exist_ok=True)

plt.savefig(f'plots/multiple_figure.png', dpi=300)

plt.clf()



