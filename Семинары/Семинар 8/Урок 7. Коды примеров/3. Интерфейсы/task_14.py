from abc import ABC, abstractmethod # нужен для проверки, что метод переопределен собственными атрибутами (хороший тон)


class MyAbstractClass(ABC):

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractClass):
    pass


mc = MyClass()

"""
TypeError: Can't instantiate abstract class MyClass with abstract methods my_method_1, my_method_2
"""
