# # class MyContext(object):
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def __enter__(self):
# #         print('调用了enter方法')
# #         return self
# #
# #     def test(self):
# #         # 1 / 0
# #         print(self.name + '调用了test方法')
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print('调用了exit方法')
# #         print(exc_type, exc_val, exc_tb)
# #
# # with MyContext('zhangsan', 18) as context:
# #     context.test()
# from email import header
#
# import requests
# s = requests.session()
# url = "https://mail.163.com/"
# s.keep_alive = False
# s.proxies = {"https": "58.253.153.201:9999", "http": "120.83.104.196:9999", }
# s.headers = header
# r = s.get(url)
# print(r.status_code)