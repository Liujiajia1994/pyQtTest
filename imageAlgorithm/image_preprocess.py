# 主要用来数据预处理：随机裁剪、尺度变换、旋转变换等
import cv2
import numpy as np
from scipy.misc import imresize
from PIL import Image
import os
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate
import random


save_file = 'E:/GitHub/pyQtTest/ImagesDataset/SAR_augument_images'


# 裁剪图片的四个角，以及中间的一块
def defined_crop(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为'+filename)
            i = i+1
            h, w = img.shape
            crop_img1 = img[1:int(3 * h / 4), 1:int(3 * w / 4)]
            crop_img2 = img[int(h / 4):h, 1:int(3 * w / 4)]
            crop_img3 = img[1:int(3 * h / 4), int(w / 4):w]
            crop_img4 = img[int(h / 4):h, int(w / 4):w]
            crop_img1 = imresize(crop_img1, (280, 280))
            crop_img2 = imresize(crop_img2, (280, 280))
            crop_img3 = imresize(crop_img3, (280, 280))
            crop_img4 = imresize(crop_img4, (280, 280))
            isExists = os.path.exists(save_file)
            if not isExists:
                os.makedirs(save_file)
            cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-crop-1.tif', crop_img1)
            cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-crop-2.tif', crop_img2)
            cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-crop-3.tif', crop_img3)
            cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-crop-4.tif', crop_img4)
            print('已保存图片')
        else:
            print('无法读取'+filename+'图片')
            returnStatus.append(filename)
    len_crop = len(returnStatus)
    results = ''
    if len_crop == 0:
        results = '随机裁剪已处理完成'
    else:
        for i in range(len_crop):
            single_result = '无法处理' + returnStatus[i] + '图片'
            results += single_result
        results += '其他已处理完成'
    return save_file, results


def check_size(size):
    if type(size) == int:
        size = (size, size)
    if type(size) != tuple:
        raise TypeError('size is int or tuple')
    return size


# 随机裁剪
def random_crop(image, crop_size):
    crop_size = check_size(crop_size)
    h, w = image.shape
    top = np.random.randint(0, h - crop_size[0])
    left = np.random.randint(0, w - crop_size[1])
    # # 随机生成不重复的整数
    # top = random.sample(range(1, 9), 1)[0]*10
    # left = random.sample(range(1, 9), 1)[0]*10
    bottom = top + crop_size[0]
    right = left + crop_size[1]
    image = image[top:bottom, left:right]
    return image


def center_crop(image, crop_size):
    crop_size = check_size(crop_size)
    h, w = image.shape
    top = (h - crop_size[0]) // 2
    left = (w - crop_size[1]) // 2
    bottom = top + crop_size[0]
    right = left + crop_size[1]
    image = image[top:bottom, left:right]
    return image


# 尺度变换
def scale_augmentation(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            crop_size = img.shape[0] if img.shape[0] < img.shape[1] else img.shape[1]
            for j in range(4):
                scale_size = int((0.2*j+1)*crop_size)
                image = imresize(img, (scale_size, scale_size))
                image = center_crop(image, crop_size)
                isExists = os.path.exists(save_file)
                if not isExists:
                    os.makedirs(save_file)
                cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-scale-'+str(j+1)+'.tif', image)
                print('已保存图片')
        else:
            print('无法读取' + filename + '图片')
            returnStatus.append(filename)
    len_scale = len(returnStatus)
    results = ''
    if len_scale == 0:
        results = '尺度变换已处理完成'
    else:
        for i in range(len_scale):
            single_result = '无法处理' + returnStatus[i] + '图片'
            results += single_result
        results += '其他已处理完成'
    return save_file, results


def resize(image, size):
    size = check_size(size)
    image = imresize(image, size)
    return image


# 旋转
def random_rotation(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            for j in range(4):
                h, w = img.shape
                angle = j*30
                image = rotate(img, angle)
                image = resize(image, (h, w))
                isExists = os.path.exists(save_file)
                if not isExists:
                    os.makedirs(save_file)
                cv2.imwrite(save_file + '/' + filename.split('.')[0] + '-rotate-' + str(j+1) + '.tif', image)
                print('已保存图片')
        else:
            print('无法读取' + filename + '图片')
            returnStatus.append(filename)
    len_rotate = len(returnStatus)
    results = ''
    if len_rotate == 0:
        results = '旋转变换已处理完成'
    else:
        for i in range(len_rotate):
            single_result = '无法处理' + returnStatus[i] + '图片'
            results += single_result
        results += '其他已处理完成'
    return save_file, results


