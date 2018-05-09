import numpy as np
import cv2
import sys

'''
============================================
ply
format ascii 1.0
element vertex 10867
property double x
property double y
property double z
property double nx
property double ny
property double nz
property uchar red
property uchar green
property uchar blue
element face 19823
property list uchar int vertex_indices
end_header
============================================
'''

# Load .xyz file
ply_file = "pointcloud/test2txt.ply"


orin_datas = np.loadtxt(ply_file)

datas = orin_datas
datas_len = len(datas)
print(datas_len)
xyz_datas = np.zeros((datas_len,3), dtype='float32')
nxyz_datas = np.zeros((datas_len,3), dtype='float32')
rgb_datas = np.zeros((datas_len,3), dtype='uint8')

# Add the data to an array.
for data_i in range(0,datas_len):
    cos_ang = datas[data_i][2] / (nxyz_datas[data_i][0] ** 2 + nxyz_datas[data_i][1] ** 2 + nxyz_datas[data_i][2] ** 2)
    if not (cos_ang <= 1 and cos_ang >= (2 ** 0.5) / 2):
    xyz_datas[data_i][0] = datas[data_i][0]
    xyz_datas[data_i][1] = datas[data_i][1]
    xyz_datas[data_i][2] = datas[data_i][2]

    nxyz_datas[data_i][0] = datas[data_i][3]
    nxyz_datas[data_i][1] = datas[data_i][4]
    nxyz_datas[data_i][2] = datas[data_i][5]

    rgb_datas[data_i][0] = datas[data_i][6]
    rgb_datas[data_i][1] = datas[data_i][7]
    rgb_datas[data_i][2] = datas[data_i][8]

# Delete the data which normal is over 45 degree between the vertical
for data_j in range(0,datas_len):
    cos_ang = datas[data_j][2]/(nxyz_datas[data_j][0]**2+ nxyz_datas[data_j][1]**2 +  nxyz_datas[data_j][2]**2)
    if not (cos_ang <=1 and cos_ang >= (2**0.5)/2):
        print(1)
        xyz_datas = np.delete(xyz_datas, data_j, 0)

        nxyz_datas = np.delete(nxyz_datas, data_j, 0)

        rgb_datas = np.delete(rgb_datas,data_j, 0)



print(xyz_datas[0][0])
xyz_datas = np.delete(xyz_datas, 1, 0)
print(xyz_datas[0][0])

