import matplotlib.pyplot as plt
import numpy as np

def set_axes_equal(ax: plt.Axes):
    """Set 3D plot axes to equal scale.

    Make axes of 3D plot have equal scale so that spheres appear as
    spheres and cubes as cubes.  Required since `ax.axis('equal')`
    and `ax.set_aspect('equal')` don't work on 3D.
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)

def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])

def plot_camera(ax):
    w = 0.2
    h = w * 0.75
    z = w * 0.6
    x = [0, w, w, -w, -w]
    y = [0, h, -h, -h, h]
    z = [0, z, z, z, z]
    O, A, B, C, D = zip(x, y, z)

    lines_1 = zip(O, A, B, C, D, A)
    lines_2 = zip(O, B, O, C, O, D)

    ax.plot3D(*lines_1,
              zdir='z',    #
              c='k',    # color
              marker='o',    # 标记点符号
              mfc='r',    # marker facecolor
              mec='g',    # marker edgecolor
              ms=10,    # size
              )
    ax.plot3D(*lines_2,
              zdir='z',    #
              c='k',    # color
              marker='o',    # 标记点符号
              mfc='r',    # marker facecolor
              mec='g',    # marker edgecolor
              ms=10,    # size
              )


def plot_axis(ax, p):
    color = ['r', 'g', 'b']
    for i in range(1, len(p)):
        line = [(p[0][0], p[i][0]), (p[0][1], p[i][1]), (p[0][2], p[i][2])]
        ax.plot3D(line[0], line[1], line[2], c=color[i-1])


def plotPyramid(ax, p):
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if (i == 0) or (j-i == 1) or (j-i == 3):
                line = [(p[i][0], p[j][0]), (p[i][1], p[j][1]), (p[i][2], p[j][2])]
                ax.plot3D(line[0], line[1], line[2], c='k')
