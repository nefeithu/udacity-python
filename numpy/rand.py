import numpy as np
import numpy.random as random

# 设置随机数种子，随机数确定
random.seed(42)

print('Random number with seed 42: ', random.random())

# 产生一个1x3，[0,1)之间的浮点型随机数
# array([[ 0.37454012,  0.95071431,  0.73199394]])
# 后面的例子就不在注释中给出具体结果了
print('random.rand(1, 3) = ',random.rand(1, 3))

# 产生一个[0,1)之间的浮点型随机数
print('Random number with no seed: ', random.random())

# 下边4个没有区别，都是按照指定大小产生[0,1)之间的浮点型随机数array，不Pythonic…
print('random.random((3, 3))=',random.random((3, 3)))
print('random.sample((3, 3))=',random.sample((3, 3)))
print('random.random_sample((3, 3))=',random.random_sample((3, 3)))
print('random.ranf((3, 3))=',random.ranf((3, 3)))

# 产生10个[1,6)之间的浮点型随机数
5*random.random(10) + 1
random.uniform(1, 6, 10)

# 产生10个[1,6)之间的整型随机数
random.randint(1, 6, 10)

# 产生2x5的标准正态分布样本
result = random.normal(size=(5, 2))
print('random.normal(size=(5, 2))=', result)

# 产生5个，n=5，p=0.5的二项分布样本
random.binomial(n=5, p=0.5, size=5)

a = np.arange(10)

# 从a中有回放的随机采样7个
random.choice(a, 7)

# 从a中无回放的随机采样7个
random.choice(a, 7, replace=False)

# 对a进行乱序并返回一个新的array
b = random.permutation(a)

# 对a进行in-place乱序
random.shuffle(a)

# 生成一个长度为9的随机bytes序列并作为str返回
# '\x96\x9d\xd1?\xe6\x18\xbb\x9a\xec'
random.bytes(9)