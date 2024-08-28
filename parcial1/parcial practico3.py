class Apps:
    def __init__(self,tipo,peso):
        self.tipo= tipo
        self.peso= peso
        

instagram = Apps("social","30Mb")
Brawlstarts = Apps("juego en linea","590.81Mb")

print(type(instagram))
print(type(Brawlstarts))

print(instagram.tipo,instagram.peso)
print(Brawlstarts.tipo,Brawlstarts.peso)