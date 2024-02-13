#CONJUNTOS
set = {1,2,3,3,4}
print(set)

#DICCIONARIOS
diccionario = {
    "numero1": 1,
    "nombre": "David"
}
print(diccionario.get("nombre"))

#CLASES
class Carro():
    marca = "Chevrolet"
    
    def mostrarMarca(self):
        print(self.marca)

class Deportivo(Carro):
    marca= "Ferrari"
carro = Carro()
deportivo = Deportivo()
carro.mostrarMarca()
deportivo.mostrarMarca()