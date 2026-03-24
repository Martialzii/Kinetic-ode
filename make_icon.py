import numpy as np
import matplotlib.pyplot as plt

# 1. Define a Kinetic System (Van der Pol Oscillator - Classic Engineering ODE)
def vdp(X, t=0):
    mu = 1.5
    return np.array([X[1], mu*(1 - X[0]**2)*X[1] - X[0]])

# 2. Create the Grid
x = np.linspace(-3, 3, 25)
y = np.linspace(-3, 3, 25)
X, Y = np.meshgrid(x, y)
u, v = np.zeros(X.shape), np.zeros(Y.shape)

for i in range(len(x)):
    for j in range(len(y)):
        res = vdp([X[i,j], Y[i,j]])
        u[i,j], v[i,j] = res[0], res[1]

# 3. Plotting the "Asset"
plt.figure(figsize=(10, 6), facecolor='#0d1117') 
ax = plt.axes()
ax.set_facecolor('#0d1117')
plt.streamplot(X, Y, u, v, color='#58a6ff', linewidth=1, density=1.5)
plt.axis('off')

# 4. Save for GitHub Social Preview
plt.savefig('sidebar_icon.png', dpi=150, bbox_inches='tight', pad_inches=0)
print("Asset Created: sidebar_icon.png")