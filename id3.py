from math import log
import operator


def calcShannonEnt(dataSet):  # 计算数据的信息熵(entropy)
    numEntries = len(dataSet)  # 数据条数
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0  # 这一步其实就是在字典里面初始化每个类别的个数
        labelCounts[currentLabel] += 1  # 统计有多少个类以及每个类的数量
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries  # 计算单个类的熵值
        shannonEnt -= prob * log(prob, 2)  # 累加每个类的熵值
    return shannonEnt


def createDataSet1():  # 创造示例数据
    dataSet = [['长', '粗', '男'],
               ['短', '粗', '男'],
               ['短', '粗', '男'],
               ['长', '细', '女'],
               ['短', '细', '女'],
               ['短', '粗', '女'],
               ['长', '粗', '女'],
               ['长', '粗', '女']]
    features = ['头发', '声音']  # 两个特征
    return dataSet, features


def splitDataSet(data_set, axis, value):  # 按某个特征分类后的数据
    retDataSet = []
    for featVec in data_set:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])  # 这两步的操作是没有包括划分的特征属性 很微妙！
            retDataSet.append(reducedFeatVec)

    return retDataSet


def chooseBestFeatureToSplit(data_set):  # 选择最优的分类特征
    numFeatures = len(data_set[0]) - 1  # 获得特征的个数  2个
    baseEntropy = calcShannonEnt(data_set)  # 原始的信息熵
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历两个特征
        featList = [example[i] for example in data_set]
        uniqueVals = set(featList)  # 引入集合
        newEntropy = 0

        for value in uniqueVals:
            subDataSet = splitDataSet(data_set, i, value)  # 根据某个特征分类后的数据集
            prob = len(subDataSet) / float(len(data_set))
            newEntropy += prob * calcShannonEnt(subDataSet)  # 按特征分类后的条件经验熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值 即按照这个特征划分后的信息增益
        if infoGain > bestInfoGain:  # 若按某特征划分后，熵值减少的最大，则次特征为最优分类特征
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature  # 返回的是最优特征的索引


def majorityCnt(classList):  # 按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # print(sortedClassCount)
    return sortedClassCount[0][0]


# 构建决策树(ID3决策树)
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0]) == len(classList):  # 最终叶子结点中都是一个类别的话就return那个类别
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最优特征的索引
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}  # 分类结果以字典形式保存
    del (labels[bestFeat])  # labels中只有头发这个属性了
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)  # {'粗'，'细'}、{'长','短'}
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


if __name__ == '__main__':
    dataSet, labels = createDataSet1()  # 创造示列数据
    print(createTree(dataSet, labels))  # 输出决策树模型结果
