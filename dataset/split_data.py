import os
import random
import shutil

# 设置文件夹路径
images_folder = r'F:\study\dataset\tiaozhansai_precoss\images'
labels_folder = r'F:\study\dataset\tiaozhansai_precoss\labels'
save_name = r'F:\study\dataset\tiaozhansai_coco'
save_name11 = 'images'
save_name12 = 'train'
save_name21 = 'labels'
save_name22 = 'val'

# 设置训练文件和测试文件的比例
train_ratio = 0.8  # 训练文件比例
test_ratio = 0.2  # 测试文件比例

# 获取images文件夹中的文件列表
image_files = os.listdir(images_folder)

# 随机打乱文件列表
random.shuffle(image_files)

# 计算训练文件和测试文件的数量
train_count = int(len(image_files) * train_ratio)
test_count = len(image_files) - train_count

# 创建训练文件夹和测试文件夹
os.makedirs(os.path.join(save_name,save_name11, save_name12), exist_ok=True)
os.makedirs(os.path.join(save_name,save_name11, save_name12), exist_ok=True)
os.makedirs(os.path.join(save_name,save_name11, save_name22), exist_ok=True)
os.makedirs(os.path.join(save_name,save_name21, save_name12), exist_ok=True)
os.makedirs(os.path.join(save_name,save_name21, save_name22), exist_ok=True)

# 将文件分配到训练文件夹和测试文件夹
for i, image_file in enumerate(image_files):
    image_path = os.path.join(images_folder, image_file)
    label_path = os.path.join(labels_folder, image_file.replace('.jpg','.txt'))  # 假设labels文件夹中的文件与images文件夹中的文件对应

    if i < train_count:
        # 将文件复制到训练文件夹
        shutil.copy(image_path, os.path.join(save_name,save_name11, save_name12))
        shutil.copy(label_path, os.path.join(save_name,save_name21, save_name12))

    else:
        # 将文件复制到测试文件夹
        shutil.copy(image_path, os.path.join(save_name,save_name11, save_name22))
        shutil.copy(label_path, os.path.join(save_name,save_name21, save_name22))

