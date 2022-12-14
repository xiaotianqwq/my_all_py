# -*- coding = utf-8 -*-
# @Time:2022/10/18 9:35
# @Author:宇
# @File:1.sklearn数据集.py
# @Software:PyCharm
from sklearn import datasets
from sklearn import model_selection
from sklearn import feature_extraction
from sklearn import preprocessing
from sklearn import feature_selection
from sklearn import decomposition
from scipy.stats import pearsonr
import jieba
import pandas as pd


def datasets_demo():
    """
    sklearn数据集的使用
    :return:
    """
    # 获取数据集
    iris = datasets.load_iris()
    print('莺尾花数据集：\n', iris)
    # print('莺尾花数据集描述：\n', iris['DESCR'])
    # print('莺尾花特征值名称：\n', iris.feature_names)
    # print('莺尾花特征值：\n', iris.data, iris.data.shape)
    x_train, x_text, y_train, y_test = model_selection.train_test_split(iris.data, iris.target, train_size=0.8,
                                                                        random_state=10)
    print('莺尾花数据集划分的测试集的特征值：\n', x_train, x_train.shape)
    return None


def dict_dome():
    data = [
        {'city': '北京', 'temperature': 30},
        {'city': '深圳', 'temperature': 23},
        {'city': '天津', 'temperature': 32}
    ]
    # 1.实例化一个转换器
    transfer = feature_extraction.DictVectorizer(sparse=True)  # sparse=False 使输出结果为矩阵，而不是稀疏矩阵
    # 2.调用fit_transform
    data_now = transfer.fit_transform(data)
    print('data_now:\n', data_now.toarray())
    print('特征名称:\n', transfer.get_feature_names_out())
    return None


def count_dome():
    data = [
        'Life is short,i like python',
        'Life is too long,i dislike python'
    ]
    # 1.实例化一个转换器
    transfer = feature_extraction.text.CountVectorizer()
    # 2.调用fit_transform
    data_now = transfer.fit_transform(data)
    print('data_now:\n', data_now.toarray())
    print('特征名称:\n', transfer.get_feature_names_out())
    return None


def cut_word(text):
    """
    中文分词 返回字符串
    :param text:
    :return:
    """
    return ' '.join(jieba.cut(text))


def count_zh_dome():
    data = [
        '有时候我也会问自己，为啥喜欢老哥视频？这个视频后我明确了答案，是因为老哥和王老师的日常，是我向往的爱情',
        '我现在的状态就跟gh最后说的一样了，但是我相信我们一定会度过这一段时间的。这段时间很苦，但没有你的未来会更苦',
        '本地人现身说法，广州游艇不行，建议买卖渔艇，艇仔粥非常出名，行业蒸蒸日上，欢迎前来投资，做大做强，共创辉煌'
    ]
    data_new = []
    for i in data:
        data_new.append(cut_word(i))
    # 1.实例化一个转换器
    transfer = feature_extraction.text.CountVectorizer()
    # 2.调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print('data_now:\n', data_final.toarray())
    print('特征名称:\n', transfer.get_feature_names_out())
    return None


def tfidf_dome():
    data = [
        '有时候我也会问自己，为啥喜欢老哥视频？这个视频后我明确了答案，是因为老哥和王老师的日常，是我向往的爱情',
        '我现在的状态就跟gh最后说的一样了，但是我相信我们一定会度过这一段时间的。这段时间很苦，但没有你的未来会更苦',
        '本地人现身说法，广州游艇不行，建议买卖渔艇，艇仔粥非常出名，行业蒸蒸日上，欢迎前来投资，做大做强，共创辉煌'
    ]
    data_new = []
    for i in data:
        data_new.append(cut_word(i))
    # 1.实例化一个转换器
    transfer = feature_extraction.text.TfidfVectorizer()
    # 2.调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print('data_now:\n', data_final.toarray())
    print('特征名称:\n', transfer.get_feature_names_out())
    return None


def minmax_dome():
    """
    数据归一化
    :return:
    """
    # 1.得到数据
    data = pd.read_csv('dating.txt', sep='\t')
    print(data)
    data = data.iloc[:, :3]
    # 2.实例化对象
    transfer = preprocessing.MinMaxScaler()
    # 3.fit_transform转换
    data_new = transfer.fit_transform(data)
    print('data:\n', data_new)

    return None


def standard_dome():
    """
    数据标准化
    :return:
    """
    # 1.得到数据
    data = pd.read_csv('dating.txt', sep='\t')
    print(data)
    data = data.iloc[:, :3]
    # 2.实例化对象
    transfer = preprocessing.StandardScaler()
    # 3.fit_transform转换
    data_new = transfer.fit_transform(data)
    print('data:\n', data_new)

    return None


def variance_dome():
    """
    过滤低方差差特征
    :return:
    """
    # 1.得到数据
    data = pd.read_csv('factor_returns.csv')
    data = data.iloc[:, 1:-2]
    print(data)
    # 2.实例化对象
    transfer = feature_selection.VarianceThreshold(threshold=0)
    # 3.fit_transform转换
    data_now = transfer.fit_transform(data)
    print(data_now)
    # 相关系数的计算
    r = pearsonr(data['pe_ratio'],data['pb_ratio'])
    print('相关系数是:', r)
    return None


def pearsonr_demo():
    """
    两两特征的相关系数
    :return:
    """
    data = pd.read_csv('factor_returns.csv')
    factor = ['pe_ratio', 'pb_ratio', 'market_cap', 'return_on_asset_net_profit', 'du_return_on_equity', 'ev',
              'earnings_per_share', 'revenue', 'total_expense']

    for i in range(len(factor)):
        for j in range(i + 1, len(factor)):
            print('%s特征与%s特征的相关系数为%f' %(factor[i], factor[j], pearsonr(data[factor[i]], data[factor[j]])[0]))
    return None


def PCA_dome():
    """
    PCA降维
    :return:
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # 实例化PCA,小数——保留多少信息
    transfer = decomposition.PCA(n_components=0.9)
    # 调用fit_transform
    data_new1 = transfer.fit_transform(data)
    print('保留90%的信息，降维的结果为:\n', data_new1)

    # 实例化PCA,整数——指定降维到的维数
    transfer = decomposition.PCA(n_components=3)
    # 调用fit_transform
    data_new2 = transfer.fit_transform(data)
    print('降维到3维的结果为:\n', data_new2)
    return None


if __name__ == '__main__':
    # datasets_demo()
    # dict_dome()
    # count_dome()
    # cut_word('有时候我也会问自己，为啥喜欢老哥视频？这个视频后我明确了答案，是因为老哥和王老师的日常，是我向往的爱情')
    # count_zh_dome()
    # tfidf_dome()
    # minmax_dome()
    # standard_dome()
    # variance_dome()
    # pearsonr_demo()
    PCA_dome()