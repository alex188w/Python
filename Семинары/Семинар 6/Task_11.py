# найти элементы, не имеющие дублей
"""
lst = [1, 2, 3, 5, 1, 5, 3, 10] -> [2, 10]
"""

# 1
lst = [1, 2, 3, 5, 1, 5, 3, 10] 
# res = list(filter(lambda i: lst.count(i) == 1, lst))
# print(res)


# 2
def sort(lst):
    uniq_element = set()
    for el in lst:
        if el not in uniq_element:
            uniq_element.add(el) # добавление элемента
        else: 
            uniq_element.giscard(el) # удаление элемента
    res = list(uniq_element)
    res.sort()
    print(res) 
    return res
       
sort(lst)