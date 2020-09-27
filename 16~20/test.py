class MyContext(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        print('调用了enter方法')
        return self

    def test(self):
        # 1 / 0
        print(self.name + '调用了test方法')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('调用了exit方法')
        print(exc_type, exc_val, exc_tb)

with MyContext('zhangsan', 18) as context:
    context.test()