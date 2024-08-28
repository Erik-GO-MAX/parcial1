#parcial practico 1
class Dispositivo:
    def __init__(self,marca,modelo,color):
        self.marca= marca
        self.modelo= modelo
        self.color= color

Honor = Dispositivo("Honor","X8B","negro")
oppo = Dispositivo("oppo","reno 11","gris")

print(type(Honor))
print(type(oppo))

print(Honor.marca,Honor.modelo,Honor.color)
print(oppo.marca,oppo.modelo,oppo.color)