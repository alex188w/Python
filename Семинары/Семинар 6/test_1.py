# Есть произвольная строка 223 + 2 


# Разбиваем (распарсиванем), разбираем на элементы (массив) и считаем
def parse(s):
    result = []
    digit = ''
    for symb in s:                  # У цикла for тожже есть else!!!
        if symb.isdigit():
            digit += symb
        elif symb in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symb)
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symb)
    else:
        if digit:
            result.append(float(digit))
    return result


print(parse('(1+2)*2')) # Результат: ['(', 1.0, '+', 2.0, ')', '*', 2.0]


# Считываем маасив и производим вычисления!!!
def calc(lst):
    result = 0.0
    while '*' in lst: # находим опрератор *
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1] # перемножаем то что слева и спрва
        lst = lst[:index - 1] + [result] + lst[index + 2:] # записываем новый массив без этих элементов
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:] # записываем новый массив без этих элементов
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def brackets(lst):
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calc(lst[opening + 1:closing])] + lst[closing + 1:]
    return lst


s = "(1+2)*3"
result = parse(s)
result = brackets(result)
print(calc(result))