# import necessary module
from file_io import *
from coordinate_transformation import *
from visualization import *
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
os.system("")  # 这是玄学的关键，在执行完system()之后，转移序列都会生效，原因未知


# step1: load data from file
# you replace this using with open
print('\033[0;36m====step1: loaddata begin ====\033[0m')
file = "./data/data_tum.txt"
time_list, trans_list, quat_list = read_data_tum(file)
file = "./data/dataset/poses/02.txt"
trans_list, rot_list = read_data_kitti(file)

print('\033[0;36m====step1: loaddata end ====\033[0m')

# # new a figure and set it into 3d
fig = plt.figure()
ax = Axes3D(fig)

scale = 0.1
point_axis = scale * np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
# plot_axis(ax, point_axis)
point_pyramid = scale * np.array(
    [[0, 0, 0], [-1, 0.75, 0.6], [1, 0.75, 0.6], [1, -0.75, 0.6], [-1, -0.75, 0.6]])
# plotPyramid(ax, point_pyramid)
T_init = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
                  [0, 0, 0, 1]])
ax.plot3D(trans_list[:, 0],
          trans_list[:, 1], trans_list[:, 2])
# for i in range(0, len(time_list), 50):
#     # print(i)
#     t = trans_list[i]
#     q = quat_list[i]
#     T_cur = Tmatrix(qvec2rotmat(q), t)

#     point_axis_hom = np.concatenate(
#         (point_axis, np.array([[1.], [1.], [1.], [1.]])), axis=1)
#     for j in range(0, point_axis_hom.shape[0]):
#         point_axis_hom[j, :] = np.dot(T_cur, point_axis_hom[j].T)
#     # print('point_axis_hom:', point_axis_hom)
#     plot_axis(ax, point_axis_hom)

#     point_pyramid_hom = np.concatenate(
#         (point_pyramid, np.array([[1.], [1.], [1.], [1.], [1.]])), axis=1)
#     for j in range(0, point_pyramid_hom.shape[0]):
#         point_pyramid_hom[j, :] = np.dot(T_cur, point_pyramid_hom[j].T)
#     # print('point_pyramid_hom:', point_pyramid_hom)
#     plotPyramid(ax, point_pyramid_hom)


ax.set_xlabel('X', color='r')
ax.set_ylabel('Y', color='r')
ax.set_zlabel('Z', color='r')

# set_axes_equal(ax)
plt.show()


# # ############ first subplot ############
# ax = fig.add_subplot(2, 2, 1, projection='3d')

# ax.set_title("3D_Curve1")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
