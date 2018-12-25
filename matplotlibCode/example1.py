import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline<matplotlib.legend.Legend at 0x7fb04841ce80>
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib import font_manager as fm
# prop = fm.FontProperties(fname="")
fig, ax = plt.subplots()
Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
]
codes, verts = zip(*path_data)
print(type(codes))
print(type(verts))
print(verts)
print(codes)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5) # color
ax.add_patch(patch)
# x, y = zip(*path.vertices)
ax.grid()
ax.axis('equal')
plt.title('heart')
plt.show()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),'k',label = 'one')
ax.plot(np.random.randn(1000).cumsum(), 'k--', label = 'two')
ax.plot(np.random.randn(1000).cumsum(), 'k.', label = 'three')
ax.legend()
plt.show()
