#! python 3
# Author: Zhou Xinyu

'''
===============================================================================
We have the .xyz file, which has been modified the viewpoint.
Using this .xyz file, we can get a pointcloud of some leaves.
And after modified the viewpoint we can have pointcloud which can easily gain the projection.
Using this code, we will change the pointcloud to a rgbd-image by projection.
===============================================================================
'''

import numpy as np
import cv2
import sys

# Load .xyz file
xyz_file = "pointcloud/tree_test_orth_test_2.xyz"

orin_datas = np.loadtxt(xyz_file)
orin_len = len(orin_datas)

# Get the filtered point cloud
# datas = []
# for orin_i in range(0, orin_len):
#     if orin_datas[orin_i][2] <= 0.2 and orin_datas[orin_i][2] >= -0.5:
#         datas.append(orin_datas[orin_i])

datas = orin_datas

print ("Load finished")

datas_len = len(datas)
xyz_datas = np.zeros((datas_len,3), dtype='float32')
rgb_datas = np.zeros((datas_len,3), dtype='uint8')
for data_i in range(0,datas_len):
    xyz_datas[data_i][0] = datas[data_i][0]
    xyz_datas[data_i][1] = datas[data_i][1]
    xyz_datas[data_i][2] = datas[data_i][2]
    rgb_datas[data_i][0] = datas[data_i][3]
    rgb_datas[data_i][1] = datas[data_i][4]
    rgb_datas[data_i][2] = datas[data_i][5]


min_x = xyz_datas[0][0]
for xyz_data_i in range(0,datas_len):
    if min_x > xyz_datas[xyz_data_i][0]:
        min_x = xyz_datas[xyz_data_i][0]

max_x = xyz_datas[0][0]
for xyz_data_i in range(0,datas_len):
    if max_x < xyz_datas[xyz_data_i][0]:
        max_x = xyz_datas[xyz_data_i][0]

min_y = xyz_datas[0][1]
for xyz_data_i in range(0,datas_len):
    if min_y > xyz_datas[xyz_data_i][1]:
        min_y = xyz_datas[xyz_data_i][1]

max_y = xyz_datas[0][1]
for xyz_data_i in range(0,datas_len):
    if max_y < xyz_datas[xyz_data_i][1]:
        max_y = xyz_datas[xyz_data_i][1]

min_z = xyz_datas[0][2]
for xyz_data_i in range(0,datas_len):
    if min_z > xyz_datas[xyz_data_i][2]:
        min_z = xyz_datas[xyz_data_i][2]

max_z = xyz_datas[0][2]
for xyz_data_i in range(0,datas_len):
    if max_z < xyz_datas[xyz_data_i][2]:
        max_z = xyz_datas[xyz_data_i][2]

L_x = max_x - min_x
L_y = max_y - min_y

# Image size
rgb_img = np.zeros((1000,1000,3), dtype='uint8')
dep_img = np.zeros((1000,1000), dtype='uint8')

# Resolution for rgb image and depth image
ImgRes = max(L_x , L_y)/1000
Depth_z = (max_z - min_z)/(2**8)

print ("Resolution got")

for img_i in range(0,datas_len):
    x_pos = int((xyz_datas[img_i][0] - min_x)//ImgRes)
    y_pos = int((xyz_datas[img_i][1] - min_y)//ImgRes)
    if (x_pos >= 1000):
        x_pos = 999
    if (y_pos >= 1000):
        y_pos = 999

    rgb_img[x_pos][y_pos][2] = rgb_datas[img_i][0]
    rgb_img[x_pos][y_pos][1] = rgb_datas[img_i][1]
    rgb_img[x_pos][y_pos][0] = rgb_datas[img_i][2]

    dep_img[x_pos][y_pos] = (xyz_datas[img_i][2] - min_z)//Depth_z

# save images
cv2.imwrite("images/tree_dep_4.png", dep_img)
cv2.imwrite("images/tree_rgb_4.png", rgb_img)

print("finished!")
