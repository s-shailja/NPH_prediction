#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
initial_img_dir = "/home/fei/NPH_data/Initial/"
initial_files = os.listdir(initial_img_dir)
final_img_dir = "/home/fei/NPH_data/Segmentations/"
final_files = os.listdir(final_img_dir)
raw_img_dir = "/home/fei/NPH_data/Scans/"
raw_files = os.listdir(raw_img_dir)


# In[7]:


#Final files
import nibabel as nib
for file in final_files:
    if ".nii" in file:
        final_img = nib.load(final_img_dir + file )
        final_N = final_img.get_fdata()
        max_z = 0
        count_z = 0
        for k in range(final_N.shape[2]):
            count = 0
            for i in range(final_N.shape[0]):
                for j in range(final_N.shape[1]):
                    if (final_N[i][j][k] ==1 or final_N[i][j][k] == 6):
                        count += 1
            if (count > count_z):
                max_z = k
                count_z = count
        count_csf_list = []
        count_ventricle_list = []
        for k in range(max_z-3,max_z+4):
            count_csf = 0
            count_ventricle = 0
            count_grey = 0
            for i in range(final_N.shape[0]):
                for j in range(final_N.shape[1]):
                    if (final_N[i][j][k] ==1 or final_N[i][j][k] == 3 or final_N[i][j][k] == 6):
                        count_csf += 1
                    if (final_N[i][j][k] ==1  or final_N[i][j][k] == 6):
                        count_ventricle += 1
                    if (final_N[i][j][k] == 2):
                        count_grey += 1
            count_csf_list.append(count_csf*1.0/count_grey)
            count_ventricle_list.append(count_ventricle*1.0/count_grey)

        print(file, max(count_csf_list), max(count_ventricle_list))


# In[ ]:


#Initial Files
import nibabel as nib
for file in initial_files:
    try:
        final_img = nib.load(initial_img_dir + file )
        final_N = final_img.get_fdata()
        max_z = 0
        count_z = 0
        for k in range(final_N.shape[2]):
            count = 0
            for i in range(final_N.shape[0]):
                for j in range(final_N.shape[1]):
                    if (final_N[i][j][k] ==1 or final_N[i][j][k] == 6):
                        count += 1
            if (count > count_z):
                max_z = k
                count_z = count
    #     print(file, max_z)
        count_csf_list = []
        count_ventricle_list = []
        for k in range(max_z-3,max_z+4):
            count_csf = 0
            count_ventricle = 0
            count_grey = 0
            for i in range(final_N.shape[0]):
                for j in range(final_N.shape[1]):
                    if (final_N[i][j][k] ==1 or final_N[i][j][k] == 3 or final_N[i][j][k] == 6):
                        count_csf += 1
                    if (final_N[i][j][k] ==1  or final_N[i][j][k] == 6):
                        count_ventricle += 1
                    if (final_N[i][j][k] == 2):
                        count_grey += 1
            count_csf_list.append(count_csf*1.0/count_grey)
            count_ventricle_list.append(count_ventricle*1.0/count_grey)

        print(file, max(count_csf_list), max(count_ventricle_list))
    except:
        pass

