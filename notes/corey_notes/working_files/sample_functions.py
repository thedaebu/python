def add(a, b):
    return a+b

def divide(a, b):
    if b == 0:
        raise ValueError('Denominator cannot be zero')
    return a / b