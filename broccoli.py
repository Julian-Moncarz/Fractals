import matplotlib.pyplot as plt
import numpy as np

def broccoli_fractal(order, length=1.0):
    angle = np.pi / 3
    p1 = np.array([0, 0])
    p2 = np.array([length, 0])
    p3 = np.array([length / 2, length * np.sin(angle)])
    points = np.array([p1, p2, p3, p1])

    def broccoli_iteration(points):
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            pA = p1 + (p2 - p1) / 3
            pB = p1 + 2 * (p2 - p1) / 3
            dx, dy = pB - pA
            scale = np.sqrt(3) / 2
            pC = pA + np.array([-dy * scale, dx * scale])
            pD = pB + np.array([dy * scale, -dx * scale])
            new_points.extend([p1, pA, pC, pB, pD])
        new_points.append(points[-1])
        return np.array(new_points)

    for _ in range(order):
        points = broccoli_iteration(points)

    return points

order = 5
length = 1.0

points = broccoli_fractal(order, length)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'g-')
plt.axis('equal')
plt.title(f"Broccoli Fractal (Order {order})")
plt.savefig("broccoli_fractal.png")
