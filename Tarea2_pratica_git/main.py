from calculadora import *

option = input(
    """
Seleccione una operación
1. Suma 
2. Resta
3. Multiplicacion
4. Division
"""
)

try:
    option = int(option)
except:
    print("valor no valido")

if option not in [1, 2, 3, 4]:
    print("Valor no valido")
    exit()
else:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    opciones = {
        1: suma(a, b),
        2: resta(a, b),
        3: multiplicacion(a, b),
        4: division(a, b),
    }
    resultado = opciones.get(int(option))
    print(f"El resultado es : {resultado}")