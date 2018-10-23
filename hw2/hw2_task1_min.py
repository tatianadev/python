def min(arg, *args, key=None, **kwargs):  # определение функции min, в которую передаются аргументы:
    # arg, *args(кортеж), переменная key со значением по умолчанию None, **kwargs(словарь)
    if args:  # если в кортеже args есть значения, т.е. в функцию min переданы значения, относящиеся к args
        flag = False  # значение переменной flag устанавливается равным False
        iterable = args  # значение кортежа args присваивается переменной iterable
        if key is None:  # если значение переменной key равно None, то:
            vmin, kmin = arg, arg  # переменным vmin, kmin присваивается значение кортежа args
        else:  # иначе
            vmin, kmin = arg, key(arg)  # переменной vmin присваивается значение кортежа arg,
            # переменной kmin присваивается значение key(arg)
    else:  # иначе, если в переменной args нет значений, то:
        flag = True  # значение переменной flag устанавливается равным True
        iterable = arg  # значение переменной arg присваивается переменной iterable
        vmin, kmin = None, None  # переменным vmin, kmin присваивается значение None

    if key is None:  # если значение переменной key равно None
        iterable = map(lambda x: (x, x), iterable)  # при помощи функции map применяется анонимная функция lambda
        # к переменной iterable и создается map объект, содержащий кортеж из 2-х значений iterable,
        # который присваивается переменной iterable

    else:  # иначе, если значение переменной key не равно None, то:
        iterable = map(lambda x: (x, key(x)), iterable)  # при помощи функции map применяется анонимная функция lambda
        # к переменной iterable и создается map объект, содержащий кортеж из значений iterable и key(iterable),
        # который присваивается переменной iterable

    for v, k in iterable:  # для значений кортежа iterable
        if flag:  # если переменная flag равна True, то
            vmin, kmin = v, k  # переменной vmin присваивается значение v, переменной kmin - значение k
            flag = False  # переменной flag присваивается значение False
        else:  # иначе, если значение переменной flag не равно True, то:
            if k < kmin:  # если k меньше kmin, то
                vmin, kmin = v, k  # переменной vmin присваивается значение v, переменной kmin - значение k

    if flag:  # если значение переменной flag равно True
        if 'default' in kwargs:  # если значение 'default' равно значению ключа какого либо элемента словаря kwargs
            return kwargs['default']  # то вернуть значение элемента с ключом default
        raise ValueError('arg is an empty sequence')  # иначе вывести сообщение об ошибке

    return vmin  # возвращается значение переменной vmin


empty_sequence = tuple()

value_sequence = 3, 1, 2

x, y, z = value_sequence

print(min(x, y, z))  # result: 1

print(min(value_sequence))  # result: 1

print(min(x, y, z, key=lambda v: -v))  # result: 3

print(min(value_sequence, key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1

print(min(value_sequence, default=0xE0F))  # result: 1

print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!
