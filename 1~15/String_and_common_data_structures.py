'''
Date: 20200903
Author: Wumo
'''


a, b = 5, 10
print(f'{a} * {b} = {a * b}')

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))


# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)