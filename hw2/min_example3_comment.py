def min(arg, *args, value_to_key=None, **kwargs):
    """
    В функцию min может быть передано:
    - одно или несколько значений (первое значение добавлется в переменную args, остальные - в кортеж args)
    - функция в переменной value_to_key, эта функция применяется к переданным значениям в arg и args
    - словарь(с одним или несколькими ключами и их значениями), который добавляется в переменную kwargs
    """
    """
    Если в переменной value_to_key не было передано значение, то ей присваивается значение анонимной функции,
    которая возвращает переданное ей значение, т.е. переданное значение не меняется.
    """
    if value_to_key is None:
        value_to_key = lambda x: x

    """
    Если кортеж args содержит хотя бы 1 значение, то переменной values присваивается значение args,
    переменной min_value присваивается значение переменной arg, 
    переменной min_key присваивается результат выполнения функции, переданной в value_to_key, с переменной arg,
    переменной has_initial_value присваивается значение True.
    
    Если кортеж args пустой, то переменной values присваивается значение arg,
    переменной min_value присваивается значение None, 
    переменной min_key присваивается значение None,
    переменной has_initial_value присваивается значение False.
    """
    if len(args) > 0:
        values = args
        min_value, min_key = arg, value_to_key(arg)
        has_initial_value = True
    else:
        values = arg
        min_value, min_key = None, None
        has_initial_value = False

    """
    переменной value_key_pairs присваивается значение кортежа, каждый элемент которого является кортежем, который 
    состоит из:
    - переданного значения из values и 
    - результата выполнения функции, указанной в value_to_key, от этого переданного значения из values
    """
    value_key_pairs = tuple(map(lambda x: (x, value_to_key(x)), values))

    """
    В цикле for происходит перебор значений кортежа value_key_pairs 
    (value - переданное в функцию значение(из arg или args), 
    key (результат выполнения функции value_to_key от значения arg или args)) 
    
    и в случае, если переменная has_initial_value is True 
    (т.е. переменным min_value, min_key ранее уже были присвоены значения),
    то происходит сравнение значения переменной key, в которой содержится результат выполнения функции value_to_key(x),
    и значения переменной min_key.
    Если key < min_key, то переменным min_value, min_key присваиваются значения value, key, соответствующие значению
    элемента кортежа value_key_pairs.
    Если переменная has_initial_value is False, то переменным min_value, min_key присваиваются значения value, key, 
    соответствующие значению элемента кортежа value_key_pairs и переменная has_initial_value устанавливается равной True.
    
    В данном цикле происходит сравнение и поиск значения min_key и соответствующего ему min_value.
    """
    for value, key in value_key_pairs:
        if has_initial_value:
            if key < min_key:
                min_value, min_key = value, key
        else:
            min_value, min_key = value, key
            has_initial_value = True

    """
    Если в фунцию min не было передано ни одного значения для переменных arg, args, 
    то переменная has_initial_value is False, 
    и в таком случае происходит поиск значения элемента по значению ключа 'default' в словаре kwargs.
    Если ключ со значением 'default' найдет в словаре, то возвращается значение этого ключа.
    Иначе возвращается сообщение об ошибке.
    """
    if not has_initial_value:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

    """
    Если переменная arg и/или args содержит значение, то в результате сравнения и поиска min_key 
    возвращается соответствующее значению min_key значение переменной min_value.
    """
    return min_value


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, value_to_key=lambda v: -v))  # result: 3
print(min(value_sequence, value_to_key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!
