from math import sqrt


class Figura:
    def __init__(self) -> None:
        pass

    def get_area(self):
        pass

    def get_perimetro(self):
        pass


class Cuadrado(Figura):
    lado = 0

    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def get_area(self):
        return self.lado**2

    def get_perimetro(self):
        return self.lado * 4


class Rectangulo(Figura):
    lado1 = 0
    lado2 = 0

    def __init__(self, lado1, lado2) -> None:
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2

    def get_area(self):
        return self.lado1 * self.lado2

    def get_perimetro(self):
        return self.lado1 * 2 + self.lado2 * 2


class Triangulo(Figura):
    lado1 = 0
    lado2 = 0
    lado3 = 0

    def __init__(self, lado1, lado2, lado3) -> None:
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def get_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        if s < self.lado1 or s < self.lado2 or s < self.lado3:
            return 0
        area = sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

    def get_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


def OpcionNoValida():
    print("Opcion no valida")
    Menu()


def OpcionCuadrado():
    cuadrado = Cuadrado(int(input("Ingrese el tamano lado: ")))
    print("Area: " + str(cuadrado.get_area()))
    print("Perimetro: " + str(cuadrado.get_perimetro()))


def OpcionRectangulo():
    rectangulo = Rectangulo(
        int(input("Ingrese lado 1: ")), int(input("Ingrese lado 2: "))
    )
    print("Area: " + str(rectangulo.get_area()))
    print("Perimetro: " + str(rectangulo.get_perimetro()))


def OpcionTriangulo():
    triangulo = Triangulo(
        int(input("Ingrese lado 1: ")),
        int(input("Ingrese lado 2: ")),
        int(input("Ingrese lado 3: ")),
    )
    if triangulo.get_area() == 0:
        print("El triangulo no existe")
    else:
        print("Area: " + str(triangulo.get_area()))
        print("Perimetro: " + str(triangulo.get_perimetro()))


def Menu():
    print("Seleccione la figura: \n1.Cuadrado\n2.Rectangulo\n3.Triangulo")
    opcion = input()
    switch_figura = {1: OpcionCuadrado, 2: OpcionRectangulo, 3: OpcionTriangulo}
    switch_figura.get(int(opcion), OpcionNoValida)()


Menu()
