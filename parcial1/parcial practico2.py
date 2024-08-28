class Motos:
    def __init__(self, marca, cilindraje, velocidad):
        self.marca= marca
        self.cilindraje= cilindraje
        self.velocidad=velocidad

Yamaha = Motos("MT09","890cc","240 K/h")
BMW = Motos("s1000rr","999cc","300 k/h")

print(type(Yamaha))
print(type(BMW))

print(Yamaha.marca, Yamaha.cilindraje, Yamaha.velocidad)
print(BMW.marca,BMW.cilindraje,BMW.velocidad)