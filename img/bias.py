import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots(figsize=(10, 3.5))

# main plot - data
N = 1000
x = [i * math.pi / (N // 4) for i in range(-(N // 2), (N // 2) - 1)]
y = [0.5 * (1 + math.cos(x)) for x in x]

# main plot - draw
ax.plot(x, y, zorder=3)


# scale factor
factor = 1.0
shift = 0 # in number of samples

# point 0 - selection (+3/2\pi)
n_nom = +(N // 8) * 3
n = int(n_nom * factor) + shift
# point 0 - draw
ax.scatter(x[(N // 2) + n], y[(N // 2) + n], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 0 - point annotation
ax.annotate(r"$\Delta\phi_{4n}^{+\frac{3}{2}\pi}$", xy=(x[(N // 2) + n], y[(N // 2) + n]), xytext=(-32, 6), textcoords="offset points", fontsize=12, zorder=4)
# point 0 - horizontal gray line
ax.plot([0, x[(N // 2) + n]], [y[(N // 2) + n], y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 0 - vertical gray line
ax.plot([x[(N // 2) + n], x[(N // 2) + n]], [0, y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 0 - gray dots (on both axes)
ax.scatter([0, x[(N // 2) + n]], [y[(N // 2) + n], 0], color="gray", marker="o", s=15, zorder=3)
# point 0 - arrow
ax.arrow(x=x[(N // 2) + n_nom] - (0.1 if n_nom < n else -0.1), y=0.25, dx=(x[(N // 2) + n] - x[(N // 2) + n_nom]) - (0.05 if n_nom < n else -0.05), dy=0, width=0.01, head_width=0.03, head_length=0.1, facecolor="#2D7E4C", edgecolor="none")


# point 1 - selection (-1/2\pi)
n_nom = -(N // 8) * 1
n = int(n_nom * factor) + shift
# point 1 - draw
ax.scatter(x[(N // 2) + n], y[(N // 2) + n], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 1 - point annotation
ax.annotate(r"$\Delta\phi_{4n+1}^{-\frac{1}{2}\pi}$", xy=(x[(N // 2) + n], y[(N // 2) + n]), xytext=(-45, 6), textcoords="offset points", fontsize=12, zorder=4)
# point 1 - horizontal gray line
ax.plot([0, x[(N // 2) + n]], [y[(N // 2) + n], y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 1 - vertical gray line
ax.plot([x[(N // 2) + n], x[(N // 2) + n]], [0, y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 1 - gray dots (on both axes)
ax.scatter([0, x[(N // 2) + n]], [y[(N // 2) + n], 0], color="gray", marker="o", s=15, zorder=3)
# point 1 - arrow
ax.arrow(x=x[(N // 2) + n_nom] - (0.1 if n_nom < n else -0.1), y=0.25, dx=(x[(N // 2) + n] - x[(N // 2) + n_nom]) - (0.05 if n_nom < n else -0.05), dy=0, width=0.01, head_width=0.03, head_length=0.1, facecolor="#2D7E4C", edgecolor="none")


# point 2 - selection (-3/2\pi)
n_nom = -(N // 8) * 3
n = int(n_nom * factor) + shift
# point 2 - draw
ax.scatter(x[(N // 2) + n], y[(N // 2) + n], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 2 - point annotation
ax.annotate(r"$\Delta\phi_{4n+2}^{-\frac{3}{2}\pi}$", xy=(x[(N // 2) + n], y[(N // 2) + n]), xytext=(0, 6), textcoords="offset points", fontsize=12, zorder=4)
# point 2 - horizontal gray line
ax.plot([0, x[(N // 2) + n]], [y[(N // 2) + n], y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 2 - vertical gray line
ax.plot([x[(N // 2) + n], x[(N // 2) + n]], [0, y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 2 - gray dots (on both axes)
ax.scatter([0, x[(N // 2) + n]], [y[(N // 2) + n], 0], color="gray", marker="o", s=15, zorder=3)
# point 2 - arrow
ax.arrow(x=x[(N // 2) + n_nom] - (0.1 if n_nom < n else -0.1), y=0.25, dx=(x[(N // 2) + n] - x[(N // 2) + n_nom]) - (0.05 if n_nom < n else -0.05), dy=0, width=0.01, head_width=0.03, head_length=0.1, facecolor="#2D7E4C", edgecolor="none")


# point 3 - selection (+1/2\pi)
n_nom = +(N // 8) * 1
n = int(n_nom * factor) + shift
# point 3 - draw
ax.scatter(x[(N // 2) + n], y[(N // 2) + n], color="#4094c2", edgecolor='black', marker="o", s=40, zorder=4)
# point 3 - point annotation
ax.annotate(r"$\Delta\phi_{4n+3}^{+\frac{1}{2}\pi}$", xy=(x[(N // 2) + n], y[(N // 2) + n]), xytext=(0, 6), textcoords="offset points", fontsize=12, zorder=4)
# point 3 - horizontal gray line
ax.plot([0, x[(N // 2) + n]], [y[(N // 2) + n], y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 3 - vertical gray line
ax.plot([x[(N // 2) + n], x[(N // 2) + n]], [0, y[(N // 2) + n]], color="gray", linestyle="--", zorder=2)
# point 3 - gray dots (on both axes)
ax.scatter([0, x[(N // 2) + n]], [y[(N // 2) + n], 0], color="gray", marker="o", s=15, zorder=2)
# point 3 - arrow
ax.arrow(x=x[(N // 2) + n_nom] - (0.1 if n_nom < n else -0.1), y=0.25, dx=(x[(N // 2) + n] - x[(N // 2) + n_nom]) - (0.05 if n_nom < n else -0.05), dy=0, width=0.01, head_width=0.03, head_length=0.1, facecolor="#2D7E4C", edgecolor="none")


# other
ax.set_xlim(-1.6 * math.pi, 1.6 * math.pi)
ax.set_ylim(-0.02, 1.1)

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xticks([-1.5 * math.pi, -math.pi, -0.5 * math.pi, 0, 0.5 * math.pi, math.pi, 1.5 * math.pi])
ax.set_xticklabels([r"$-\frac{3}{2}\pi$", r"$-\pi$", r"$-\frac{1}{2}\pi$", "0", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$"])

ax.set_yticks([0.5, 1])
ax.set_yticklabels([r"$\frac{P_{0}}{2}$", r"$P_{0}$"])

ax.set_xlabel(r"$\Delta\phi$ [rad]", loc="right", fontsize=8)
ax.set_ylabel("intensity", loc="top", fontsize=10)

fig.savefig("bias.png", dpi=300, bbox_inches="tight")
plt.close(fig)