class Figura():
    def __init__(self) -> None:
        pass
    
    def get_area(self):
        pass
    def get_perimetro(self):
        pass

class Triangulo(Figura):
    tamano_lado=0
    def __init__(self,tamano_lado) -> None:
        super().__init__()
        self.tamano_lado=tamano_lado
    def get_area(self):
        return super().get_area()
    