x = 0
y = 0

def init(a, b):
    global x    # - инициализация переменных, объявленных выше
    global y
    x = a
    y = b

def do_it(): 
    return x * y