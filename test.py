import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# file_name="D:/data/data/test.csv"
# #df = pd.read_csv("D:/data/data/test.csv")
# #df.dropna(axis=0)
# def load_data(file_name,delim='\t'):
#     fr=open(file_name)
#     str_arr=[line.strip().split(delim) for line in fr.readlines()]
#     dat_arr = [list(map(float, line)) for line in str_arr]
#     return np.mat(dat_arr)
# #定义PCA方法
# def pca(data_mat, topNfeat = 999999):
#     # 求平均值
#     mean_val = np.mean(data_mat, axis = 0)
#     #去中心化
#     mean_removed = mean_val - data_mat
#     # 获取协方差矩阵
#     cov_mat = np.cov(mean_removed, rowvar=0)
#     #  获取特征根及特征向量
#     eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
#     # 特征根排序
#     eigen_val_ind = np.argsort(eigen_vals)
#     # 删除解释量小的特征根
#     eigen_val_ind = eigen_val_ind[:-(topNfeat+1):-1]
#     print(eigen_val_ind)
#     # 由高到低排序
#     red_eigen_vecs = eigen_vecs[:,eigen_val_ind]
#     print(red_eigen_vecs)
#     # l新维度的数据
#     low_data_mat = mean_removed * red_eigen_vecs
#     #  获取目标向量值
#     recon_mat = (low_data_mat * red_eigen_vecs.T) + mean_val
#     return low_data_mat, recon_mat

#读取csv文件程序：
dataPath = r"D:/data/data/test.csv"
dataMat = genfromtxt(dataPath, delimiter=',')
#设计pca函数

def pca(dataMat, k):
    average = np.mean(dataMat, axis=0) #按列求均值
    m, n = np.shape(dataMat)
    meanRemoved = dataMat - np.tile(average, (m,1)) #减去均值
    normData = meanRemoved / np.std(dataMat) #标准差归一化
    covMat = np.cov(normData.T) #求协方差矩阵
    eigValue, eigVec = np.linalg.eig(covMat) #求协方差矩阵的特征值和特征向量
    eigValInd = np.argsort(-eigValue) #返回特征值由大到小排序的下标
    selectVec = np.matrix(eigVec.T[:k]) #因为[:k]表示前k行，因此之前需要转置处理(选择前k个大的特征值)
    finalData = normData * selectVec.T #再转置回来
    return finalData