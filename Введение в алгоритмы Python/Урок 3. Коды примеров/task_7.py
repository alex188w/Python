"""Простейшая хеш-таблица в Python"""

goods = dict()

goods['Диван'] = 25000
goods['Кровать'] = 7000
goods['Стул'] = 1500
goods[(1, 2)] = 1500

print(goods)  # -> {'Диван': 25000, 'Кровать': 7000, 'Стул': 1500}


sys.getsizeof(dct)