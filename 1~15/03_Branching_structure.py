'''
用户身份验证

Version: 0.1
author: Wumo
'''

# username = input('请输入用户名: ')
# password = input('请输入口令: ')
# # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
# if username == 'admin' and password == '123456':
#     print('身份验证成功!')
# else:
#     print('身份验证失败!')

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()