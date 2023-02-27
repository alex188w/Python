"""__call__"""


class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, *args, **kwargs): # чтобы вызывать объект, как обычную функцию (тоже прегрузка)
        print("!")


obj = MyClass('!')
obj()
