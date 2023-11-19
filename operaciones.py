def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print(suma(3, 2))
    print(resta(5, 4))
    print(multiplicacion(5, 6))
    print(division(10, 2))