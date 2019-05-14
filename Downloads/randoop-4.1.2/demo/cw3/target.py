#target.py


def func(a, b):
    if a >= 3:
        a += 3
        func(4, 2)
        if a <= 7:
            b -= 3
            func(4, 2)
            if b != 0:
                func(4, 2)                                                           
    return False