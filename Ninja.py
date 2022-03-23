import Mascota
from Mascota import *
class Ninja:
    # implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self, nombre, apellido, premios, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premois = premios
        self.comida_mascota = comida_mascota
        self.mascota = Mascota("Fido", "raza", "Chocolates", 100, 100)
    # implementa los siguientes métodos:
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        self.mascota.jugar()
        return self
    # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        self.mascota.comer()
        return self
    # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def banar(self):
        self.mascota.ruido()
        return self 

ninja1 = Ninja("Matt", "Damon", 3, "galletas")
ninja2 = Ninja("Leo", "D", 2, "chocolates")
ninja1.alimentar().caminar().banar()
ninja1.mascota.mostrar_info_mascota()
ninja2.mascota.mostrar_info_mascota()