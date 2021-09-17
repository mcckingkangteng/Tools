import numpy as np


def read_data_kitti(path):
    data_kitti = np.loadtxt(path)
    translation_list = data_kitti[:, 9:12]
    rotation_list = data_kitti[:, 0:9]
    return translation_list, rotation_list


def read_data_tum(path):
    data_tum = np.loadtxt(path)
    timestamp_list = data_tum[:, 0]
    translation_list = data_tum[:, 1:4]
    quaternion_list = data_tum[:, 4:8]
    return timestamp_list, translation_list, quaternion_list
