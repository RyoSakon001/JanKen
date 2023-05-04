def double(num):
    if not isinstance(num, int):
        raise TypeError('numは整数でなければなりません')
    return num * 2

b = double(lambda x: x ** 2) # ** はべき乗。float型は整数ではないのでエラーになる