import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots(figsize=(10, 3.5))

# main plot - data
N = 1000
x = [i * math.pi / (N // 4) for i in range(-(N // 2), (N // 2) - 1)]
y = [0.5 * (1 + math.cos(x)) for x in x]

# main plot - draw
ax.plot(x, y)


# point 0 - point
ax.scatter(x[N // 2], y[N // 2], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 0 - point annotation
ax.annotate(r"$(0, P_0)$", xy=(x[N // 2], y[N // 2]), xytext=(10, 0), textcoords="offset points", fontsize=12)


# point 1 - selection
n = 95
# point 1 - draw
ax.scatter(x[(N // 2) + n], y[(N // 2) + n], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 1 - point annotation
ax.annotate(r"$(\Delta\phi, P(\Delta\phi))$", xy=(x[(N // 2) + n], y[(N // 2) + n]), xytext=(8, -3), textcoords="offset points", fontsize=12)
# point 1 - horizontal gray line
ax.plot([x[(N // 2) + n], 0], [y[(N // 2) + n], y[(N // 2) + n]], color="gray", linestyle="--", zorder=3)
# point 1 - vertical gray line
ax.plot([x[(N // 2) + n], x[(N // 2) + n]], [0, y[(N // 2) + n]], color="gray", linestyle="--", zorder=3)
# point 1 - gray dots (on both axes)
ax.scatter([0, x[(N // 2) + n]], [y[(N // 2) + n], 0], color="gray", marker="o", s=15, zorder=3)
# point 1 - right arrow
ax.arrow(x=0.05, y=0.02, dx=x[(N // 2) + n] - 0.2, dy=0, width=0.01, head_width=0.03, head_length=0.1, facecolor="gray", edgecolor="none")
# point 1 - point annotation
ax.text(x[(N // 2) + n] / 2, 0.025, r"$\Delta\phi$", color="gray", ha="center", va="bottom")


# other
ax.set_ylim(-0.02, 1.1)

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xticks([-2 * math.pi, -1.5 * math.pi, -math.pi, -0.5 * math.pi, 0, 0.5 * math.pi, math.pi, 1.5 * math.pi, 2 * math.pi])
ax.set_xticklabels([r"$-2\pi$", r"$-\frac{3}{2}\pi$", r"$-\pi$", r"$-\frac{1}{2}\pi$", "0", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])

ax.set_yticks([0.5, 1])
ax.set_yticklabels([r"$\frac{P_{0}}{2}$", r"$P_{0}$"])

ax.set_xlabel(r"$\Delta\phi$ [rad]", loc="right", fontsize=8)
ax.set_ylabel("intensity", loc="top", fontsize=10)


fig.savefig("response.png", dpi=300, bbox_inches="tight")
plt.close(fig)