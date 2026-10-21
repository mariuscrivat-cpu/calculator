def adunare(a, b):
    return a + b


def scadere(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Împărțirea la zero nu este permisă")
    return a / b
