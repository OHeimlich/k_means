import sys
import numpy as np
import matplotlib.pyplot as plt
from Point import Point
import time
from random import randint
from scipy.spatial import distance


# Create data
K = 3
N = 100
g1 = [Point(0.6 + 0.6 * np.random.rand(), np.random.rand(), randint(0, K-1)) for _ in range(N)]
g2 = [Point(0.4 + 0.3 * np.random.rand(), 0.5 * np.random.rand(), randint(0, K-1)) for _ in range(N)]
g3 = [Point(0.3 * np.random.rand(), 0.3 * np.random.rand(), randint(0, K-1)) for _ in range(N)]

data = g1 + g2 + g3

colors = {0: 'b', 1: 'g', 2: 'r', 3: 'c', 4: 'm', 5: 'y', 6: 'k'}#{0: 'Blue', 1: 'Aquamarine', 2: 'Coral'}

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.title('K Means Algorithm')
plt.show(block=False)

# Draw points
for p in data:
    p.ax = ax.scatter(p.x, p.y, alpha=0.8, c=colors[p.group], edgecolors='none', s=30)
fig.canvas.draw()

centers = {0: (0,0)}
old_centers = {}
centers_points = {}

while old_centers != centers:
    old_centers = centers.copy()
    # Find centers
    for c in centers_points.values():
        c.remove()

    for k in range(K):
        x, y = np.mean([p.x for p in data if p.group == k]), np.mean([p.y for p in data if p.group == k])
        centers[k] = (x, y)
        # Draw centers
        centers_points[k] = ax.scatter(x, y, alpha=0.8, c='black', edgecolors='none', s=30, marker='x')
    fig.canvas.draw()

    # Calculate euclidean distance from points to centers
    for p in data:
        min_distance = sys.maxsize
        for k in range(K):
            dis = distance.euclidean((p.x, p.y), centers[k])
            if dis < min_distance:
                min_distance = dis
                p.group = k

    # Re-draw the points with the new group's color 
    for count, p in enumerate(data):
        p.ax.set_color(colors[p.group])
        if count % 5 == 0:
            fig.canvas.draw()
