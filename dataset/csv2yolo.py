import numpy as np
import os
import pandas as pd
import shutil

def get_csv(data_dir, csv_list):
    '''

    Args:
        data_dir: 表示输入的数据集路径
        csv_list: 表示每个数据集内的文件名的列表

    Returns:
        返回所有csv文件
    '''
    csv_dirs = []
    for i in range(len(csv_list)):
        if (csv_list[i].split(".")[-1] == "csv"):
            csv_dirs.append(os.path.join(data_dir, csv_list[i]))
    # for i in range(len(csv_dirs)):
    #     print(csv_dirs[i])
    return csv_dirs
def get_image(data_dir, data):
    '''

    Args:
        data_dir: 表示输入的数据集路径
        data: 表示每个数据集内的文件名的列表

    Returns:
        返回所有csv文件
    '''
    img_dirs = []
    for i in range(len(data)):
        if (data[i].split(".")[-1] == "jpg"):
            img_dirs.append(os.path.join(data_dir, data[i]))
    return img_dirs
def load_csv(zfill_data,save_dir,csv_dirs):
    '''
    将数据集转换成yolo格式

    '''

    for i in range(len(csv_dirs)):
        idx = zfill_data[i]
        x = pd.read_csv(csv_dirs[i],header=0,sep=",",na_values='?')
        data = np.array(x)
        data1 = np.zeros((data.shape[0],4))
        # data[:,3]
        data1[:,0] = (data[:,4]+data[:,6])/2/data[:,1]
        data1[:,1] = (data[:,5]+data[:,7])/2/data[:,2]
        data1[:,2] = (data[:,6]-data[:,4])/data[:,1]
        data1[:,3] = (data[:,7]-data[:,5])/data[:,2]

        for k in range(len(data[:3])):cls.add(data[:,3][k])
        data_cls = clsStr2Int(data[:,3])
        combined_data = np.column_stack((data_cls,data1))
        combined_data = np.column_stack((data[:,0],combined_data))
        combined_data[:,1] = np.uint8(combined_data[:,1])
        save_txt(idx,save_dir, combined_data)
        # print(data1)
def clsStr2Int(data):
    '''将分类的字符编码成数字
    ['B2', 'J20', 'B52', 'Mirage2000', 'F4', 'F14', 'Tornado', 'E2', 'JAS39']
    编码成
    [0,1,2,3,4,5,6,7,8]
    '''
    data1 = np.zeros(data.shape,dtype=int)
    for i in range(len(data)):
        data1[i] = cls_result.index(data[i])
    return data1
def save_txt(idx,save_dir, data):
    '''
    Args:
        save_dir: 保存的路径
        data: 需要保存的数据

    Returns:

    '''
    if not os.path.exists(save_dir): os.makedirs(save_dir)

    save_path = os.path.join(save_dir,idx+'.txt')
    for i in range(len(data)):
        with open(save_path, 'w') as fp:
            for j in range(data.shape[0]):
                fp.write(" ".join(map(str,data[j][1:]))+'\n')
def save_image(zfill_data,save_dir,img_dirs):
    if not os.path.exists(save_dir): os.makedirs(save_dir)
    for i in range(len(img_dirs)):
        save_name =zfill_data[i]+'.'+img_dirs[i].split(".")[-1]
        shutil.copy(img_dirs[i],os.path.join(save_dir,save_name))
def get_zfill(data):
    '''得到000001到001500的列表'''
    data1 = [str(i).zfill(6) for i in range(len(data))]
    return data1

def main():
    data_dir = r"F:\study\dataset\tiaozhansai\train"
    data_list = os.listdir(data_dir)
    label_save_dir = r'F:\study\dataset\tiaozhansai_precoss/labels'
    image_save_dir = r'F:\study\dataset\tiaozhansai_precoss/images'
    csv_dirs = get_csv(data_dir, data_list)
    img_dirs = get_image(data_dir,data_list)
    zfill_data = get_zfill(csv_dirs)
    load_csv(zfill_data,label_save_dir,csv_dirs)
    save_image(zfill_data,image_save_dir,img_dirs)
cls_result = ['B2', 'J20', 'B52', 'Mirage2000', 'F4', 'F14', 'Tornado', 'E2', 'JAS39']

cls = set()
if __name__ == '__main__':
    main()
    print(cls)