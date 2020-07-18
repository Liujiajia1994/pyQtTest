# 这里提供自己写的两篇论文的基于特征融合的识别方法
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


def featureDirSpilt(featureDir):
    glcmPath = ''
    fdPath = ''
    harrisPath = ''

    for path in featureDir:
        strTemp = path.split('_')[1]
        if strTemp.find('GLCM') >= 0:
            glcmPath = path
        elif strTemp.find('FD') >= 0:
            fdPath = path
        elif strTemp.find('Harris') >= 0:
            harrisPath = path
        else:
            pass
    return glcmPath, fdPath, harrisPath


def fearureSerialFusin(num, fold, featureDir, target_file):
    glcmPath, fdPath, harrisPath = featureDirSpilt(featureDir)
    data = ''
    # 融合
    if glcmPath != '' :
        data = glcmPath
    else:
        pass
    if fdPath != '':
        data = fdPath
    else:
        pass
    if harrisPath != '':
        data = harrisPath
    else:
        pass
    score_DT = 0
    score_SVC = 0
    score_KNN = 0
    score_MLP = 0
    score_linear_SVC =0
    score_rbf_SVC = 0
    score_poly_SVC = 0
    score_sigmoid_SVC = 0
    data = np.genfromtxt(data, dtype=str, delimiter=' ').astype(float)
    target = np.genfromtxt(target_file, dtype=str, delimiter=',').astype(int)
    # 还是采用十折交叉验证来分类
    skf = StratifiedKFold(n_splits=fold)
    for train_index, test_index in skf.split(data, target):
        X_train, X_test = data[train_index], data[test_index]
        y_train, y_test = target[train_index], target[test_index]
        # 处理成二分类
        for j in range(y_train.size):
            if y_train[j] != 0:
                y_train[j] = -1
            else:
                y_train[j] = 1
        for i in range(y_test.size):
            if y_test[i] != 0:
                y_test[i] = -1
            else:
                y_test[i] = 1
        clf_linear = SVC(kernel='linear')
        clf_linear.fit(X_train, y_train)
        print('linear_SVC分类精度：%s' % (clf_linear.score(X_test, y_test)))
        score_linear_SVC += clf_linear.score(X_test, y_test)

        clf_rbf = SVC(kernel='rbf')
        clf_rbf.fit(X_train, y_train)
        print('rbf_SVC分类精度：%s' % (clf_rbf.score(X_test, y_test)))
        score_rbf_SVC += clf_rbf.score(X_test, y_test)

        clf_poly = SVC(kernel='poly', degree=2)
        clf_poly.fit(X_train, y_train)
        print('sigmoid_SVC分类精度：%s' % (clf_poly.score(X_test, y_test)))
        score_poly_SVC += clf_poly.score(X_test, y_test)

        clf_sigmoid = SVC(kernel='sigmoid')
        clf_sigmoid.fit(X_train, y_train)
        print('sigmoid_SVC分类精度：%s' % (clf_sigmoid.score(X_test, y_test)))
        score_sigmoid_SVC += clf_sigmoid.score(X_test, y_test)

        clf_KNN = KNeighborsClassifier(n_neighbors=3)
        clf_KNN.fit(X_train, y_train)
        print('KNN分类精度：%s' % (clf_KNN.score(X_test, y_test)))
        score_KNN += clf_KNN.score(X_test, y_test)

        clf_MLP = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
        clf_MLP.fit(X_train, y_train)
        print('MLP分类精度：%s' % (clf_MLP.score(X_test, y_test)))
        score_MLP += clf_MLP.score(X_test, y_test)

        clf_DT = DecisionTreeClassifier(random_state=0)
        clf_DT.fit(X_train, y_train)
        print('DT分类精度：%s' % (clf_DT.score(X_test, y_test)))
        score_DT += clf_DT.score(X_test, y_test)
    value_linear = format(float(score_linear_SVC / fold * 100), ".5f")
    value_rbf = format(float(score_rbf_SVC /fold * 100), ".5f")
    value_poly = format(float(score_poly_SVC / fold * 100), ".5f")
    value_sigmod = format(float(score_sigmoid_SVC /fold * 100), ".5f")
    value_KNN = format(float(score_KNN /fold * 100), ".5f")
    value_MLP = format(float(score_MLP /fold * 100), ".5f")
    value_DT = format(float(score_DT /fold * 100), ".5f")
    # print('linear SVC最后的分类精度：%s' % value_linear)
    # print('rbf SVC最后的分类精度：%s' % value_rbf)
    # print('poly SVC最后的分类精度：%s' % value_poly)
    # print('sigmod SVC最后的分类精度：%s' % value_sigmod)
    # print('KNN最后的分类精度：%s' % value_KNN)
    # print('MLP最后的分类精度：%s' % value_MLP)
    # print('DT最后的分类精度：%s' % value_DT)
    return value_linear, value_rbf, value_poly, value_sigmod, value_KNN, value_MLP, value_DT



