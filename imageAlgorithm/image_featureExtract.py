from skimage.feature import greycomatrix, greycoprops, local_binary_pattern
from skimage.exposure import equalize_hist
from skimage.feature import corner_harris, corner_peaks
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from sklearn import preprocessing
import cv2
import numpy as np
import math
import os
import re


MIN_DESCRIPTOR = 18
# settings for LBP
radius = 1
n_points = 8*radius
fd_len = 67
pi = 3.1415926

# 特征信息
save_GLCM_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_GLCM.txt'
save_FD_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_FD.txt'
save_Harris_file = 'E:/GitHub/pyQtTest/ImagesDataset/feature_Harris.txt'
# 类别信息
save_target= 'E:/GitHub/pyQtTest/ImagesDataset/target.txt'

# 图片
saveDir_fd = 'E:/GitHub/pyQtTest/ImagesDataset/fd_images'
saveDir_harris = 'E:/GitHub/pyQtTest/ImagesDataset/harris_images'

# GLCM
def glcm_feature(dir):
    i = 1
    returnStatus = []
    if os.path.isfile(save_target):
        os.remove(save_target)
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
                for row in range(1):
                     for col in range(4):
                         file.write(str(contrast[row][col])+' '+str(correlation[row][col])+' '+str(energy[row][col])+' '
                                    +str(homogeneity[row][col]) +' ')
                # file.write(str(contrast)+' '+str(correlation)+' '+str(energy)+' '+str(homogeneity)+'\n')
                file.write('\n')
            file.close()
            # 写类别

            with open(save_target, 'a') as file_target:
                if re.match(r'water', filename):
                    file_target.write(str(2)+'\n')
                elif re.match(r'land', filename):
                    file_target.write(str(1)+'\n')
                else:
                    file_target.write(str(0)+'\n')
            file_target.close()
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
    if os.path.isfile(save_target):
        os.remove(save_target)
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
                # ile.write(str(harris) + '\n')
                for k in range(20):
                        file.write(str(harris[k][0])+' ')
                file.write('\n')
            file.close()
            # 写类别
            with open(save_target, 'a') as file_target:
                if re.match('water', filename):
                    file_target.write(str(2) + '\n')
                elif re.match('land', filename):
                    file_target.write(str(1) + '\n')
                else:
                    file_target.write(str(0) + '\n')
            file_target.close()
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
    if os.path.isfile(save_target):
        os.remove(save_target)
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
                # file.write(str(fds) + '\n')
                for j in range(67):
                    file.write(str(fds[j])+' ')
            file.close()
            # 写类别
            with open(save_target, 'a') as file_target:
                if re.match('water', filename):
                    file_target.write(str(2) + '\n')
                elif re.match('land', filename):
                    file_target.write(str(1) + '\n')
                else:
                    file_target.write(str(0) + '\n')
            file_target.close()
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


def draw_contour(dir):
    i = 1
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 轮廓
            ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
            image, contours, hrc = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
            cv2.imshow("show", img)
            isExists = os.path.exists(saveDir_fd)
            if not isExists:
                os.makedirs(saveDir_fd)
            cv2.imwrite(saveDir_fd + '/' + filename, img)
            # cv2.waitKey(0)
        else:
            print('无法保存第' + str(i) + '个图片')
    return saveDir_fd


def draw_corner(dir):
    i = 1
    returnStatus = []
    for filename in os.listdir(dir):
        imagePath = dir + '/' + filename
        img = cv2.imread(imagePath)
        if img is not None:
            print('第' + str(i) + '张图片为' + filename)
            i = i + 1
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 角点
            # gray_img = np.float32(gray)
            # Harris_detector = cv2.cornerHarris(gray_img, 2, 3, 0.04)
            # dst = cv2.dilate(Harris_detector, None)
            # thres = 0.01 * dst.max()
            # img[dst > thres] = [255, 0, 0]
            mandrill = equalize_hist(gray)
            # corners = corner_peaks(corner_harris(mandrill), min_distance=1)
            # 使用corner_harris获取角点
            corners = corner_peaks(corner_harris(mandrill))

            fig = plt.figure()
            plt.gray()
            plt.imshow(mandrill)
            y_corner, x_corner = zip(*corners)
            plt.plot(x_corner, y_corner, 'or')
            plt.xlim(0, mandrill.shape[1])
            plt.ylim(mandrill.shape[0], 0)
            fig.set_size_inches(np.array(fig.get_size_inches()) * 1.5)
            isExists = os.path.exists(saveDir_harris)
            if not isExists:
                os.makedirs(saveDir_harris)
            plt.savefig(saveDir_harris + '/' + filename, dpi=300)
            # plt.show()
        else:
            print('无法保存第' + str(i) + '个图片')
    return saveDir_harris
