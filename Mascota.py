class Mascota:
    # implementa __init__( name , tipo , golosinas ):
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia

    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia+=25
    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia+=5
        self.salud+=10
    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud+=5
    # ruido() - imprime el sonido que produce la mascota
    def ruido(self):
        print("miau")
    def mostrar_info_mascota(self):
        print("Tu mascota tiene salud=", self.salud, "y energia=", self.energia)