from skimage.feature import greycomatrix, greycoprops, local_binary_pattern
from skimage.exposure import equalize_hist
from skimage.feature import corner_harris
from skimage.color import rgb2gray
from sklearn import preprocessing
import cv2
import numpy as np
import math
import os


MIN_DESCRIPTOR = 18
# settings for LBP
radius = 1
n_points = 8*radius
fd_len = 67
pi = 3.1415926

save_GLCM_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_GLCM'
save_FD_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_FD'
save_Harris_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_Harris'


# GLCM
def glcm_feature(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            glcms = greycomatrix(img, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)
            contrast = greycoprops(glcms, 'contrast')
            sumCon = sumH = sumCor = sumE = 0
            # for i in range(1):
            #     for j in range(4):
            #         sumCon = contrast[i][j] +sumCon
            # averageCon = sumCon/4
            correlation = greycoprops(glcms, 'correlation')
            # for i in range(1):
            #     for j in range(4):
            #         sumCor = correlation[i][j] +sumCor
            # averageCor = sumCor/4
            energy = greycoprops(glcms, 'energy')
            # for i in range(1):
            #     for j in range(4):
            #         sumE = energy[i][j] +sumE
            # averageE = sumE/4
            homogeneity = greycoprops(glcms, 'homogeneity')
            # for i in range(1):
            #     for j in range(4):
            #         sumH = homogeneity[i][j] +sumH
            # averageHomo = sumH/4
            with open(save_GLCM_file, 'a') as file:
                # for row in range(4):
                #     for col in range(4):
                #         file.write(str(contrast[row][col])+' '+str(correlation[row][col])+' '+str(energy[row][col])+' '
                #                    +str(homogeneity[row][col]))
                file.write(str(contrast)+' '+str(correlation)+' '+str(energy)+' '+str(homogeneity)+'\n')
            file.close()
            print('第' + str(i) + '张图片提取完成')
        else:
            print('无法读取' + filename + '图片')
            returnStatus.append(filename)
    len_GLCM = len(returnStatus)
    results = ''
    if len_GLCM == 0:
        results = '灰度共生矩阵特征已全部提取完成'
    else:
        for i in range(len_GLCM):
            single_result = '无法提取' + returnStatus[i] + '图片的灰度共生矩阵'
            results += single_result
        results += '其他图片的灰度共生矩阵特征已提取完成'
    return save_GLCM_file, results


# harris特征
def harris_feature(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            mandrill = equalize_hist(rgb2gray(img))
            # corners = corner_peaks(corner_harris(mandrill), min_distance=1)
            # 使用corner_harris获取角点
            harris = corner_harris(mandrill)
            with open(save_Harris_file, 'a') as file:
                file.write(str(harris) + '\n')
            file.close()
            print('第' + str(i) + '张图片提取完成')
        else:
            print('无法读取' + filename + '图片')
            returnStatus.append(filename)
    len_Harris = len(returnStatus)
    results = ''
    if len_Harris == 0:
        results = 'Harris角点特征已全部提取完成'
    else:
        for i in range(len_Harris):
            single_result = '无法提取' + returnStatus[i] + '图片的Harris角点'
            results += single_result
        results += '其他图片的Harris角点特征已提取完成'
    return save_Harris_file, results


# LBP特征
def lbp_feature(image):
    lbp = local_binary_pattern(image, n_points, radius, method='uniform')
# 1,8,ror = 256; 1,8,uniform = 10;1,8,nri_uniform = 59;
    n_bins = int(lbp.max() + 1)
    hist, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
    return hist


# Hu不变矩特征
def hu_feature(image):
    moments = cv2.moments(image)
    humoments = cv2.HuMoments(moments)
    humoments = np.log(np.abs(humoments))  # 同样建议取对数
    # print(humoments)
    return humoments


def getCentroid(cnt):
    # (m, n) = pic.shape
    # r = 0
    # c = 0
    # count = 0
    # for i in range(0, m):
    #     for j in range(0, n):
    #         if pic[i][j] > 0:
    #             r += i
    #             c += j
    #             count += 1
    # return int(r / count), int(c / count)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print('the image coordinate parameter ', 'X:', cx)
    print('the image coordinate parameter ', 'Y:', cy)
    return cx, cy


def centroid_dist(boundarys, centroid):
    index = 0.0
    step = len(boundarys) / float(fd_len)
    dists = np.zeros(fd_len)
    for i in range(0, fd_len):
        j = int(index)
        dists[i] = eucld_metric(boundarys[j], centroid)
        index += step
    return dists


def eucld_metric(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


def FDFT(shape_signt):
    fds = np.zeros(fd_len)
    for n in range(0, fd_len):
        for i in range(0, fd_len):
            fds[n] += shape_signt[i] * math.exp(-2 * pi * i * n / fd_len)
        fds[n] /= fd_len
    return fds


def getContours(pic):
    img, contours, hrc = cv2.findContours(pic, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cts = np.array(contours[0])
    cts = cts.reshape(cts.shape[0], 2)
    return cts

# def getBoundary(pic):
#     edge = cv2.Canny(pic, 100, 250)
#     points = []
#     m, n = edge.shape
#     for i in range(0, m):
#         for j in range(0, n):
#             if edge[i][j] != 0:
#                 points.append((i, j))
#     return np.array(points)


# FD 傅里叶描述子
def fourier_descriptor_feature(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath, 0)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            # 获取轮廓
            contours = getContours(img)
            # 获取质心
            ctr = getCentroid(img)
            # the below func rise the accuracy about 3.5%
            # contours = getMaxContour(pic)
            # 计算轮廓到质心的距离
            shape_signt = centroid_dist(contours, ctr)
            # 傅立叶描述子
            fds = FDFT(shape_signt)
            with open(save_FD_file, 'a') as file:
                file.write(str(fds) + '\n')
            file.close()
            print('第' + str(i) + '张图片提取完成')
        else:
            print('无法读取' + filename + '图片')
            returnStatus.append(filename)
    len_FD = len(returnStatus)
    results = ''
    if len_FD == 0:
        results = '傅里叶描述子特征已全部提取完成'
    else:
        for i in range(len_FD):
            single_result = '无法提取' + returnStatus[i] + '图片的傅里叶描述子'
            results += single_result
        results += '其他图片的傅里叶描述子特征已提取完成'
    return save_FD_file, results


def getMaxContour(pic):
    img, contours, hrc = cv2.findContours(pic, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    max_area = 0
    max_idx = 0
    area = 0
    for i in range(0, len(contours)):
        area = cv2.contourArea(contours[i])
        if area > max_area:
            max_idx = i
            max_area = area
    cts = np.array(contours[max_idx])
    cts = cts.reshape(cts.shape[0], 2)
    return cts
