"""__setattr__"""


class MyClass:
    def __setattr__(self, attr, value):
        if attr == "width":
            self.__dict__[attr] = value # self.__dict__ - обращение к словарю атрибутов объекта, создаем атрибут и прописываем значение value (40)
        else:
            print(f"Атрибут {attr} недопустим")


mc = MyClass()
mc.width = 40  # -> Атрибут height недопустим
