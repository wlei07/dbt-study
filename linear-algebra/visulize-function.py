import numpy as np
import matplotlib.pyplot as plt

# 1) Data for the line: 2x - y = 0  ->  y = 2x
x = np.linspace(-10, 10, 400)
y = 2 * x

fig, ax = plt.subplots()

# 2) Plot the line
ax.plot(x, y)

# 3) Set visible range (so arrows have a clear end)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 4) Draw a grid
ax.grid(True)

# 5) Remove the default box/axes lines (spines)
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# 6) Keep ticks on the bottom/left (optional, but nice)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 7) Draw axis arrows (positive direction)
#    xy = arrow tip, xytext = arrow start
ax.annotate("", xy=(10, 0), xytext=(-10, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))
ax.annotate("", xy=(0, 10), xytext=(0, -10),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))

# 8) Labels and title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Line: 2x - y = 0 (y = 2x)")

plt.show()
