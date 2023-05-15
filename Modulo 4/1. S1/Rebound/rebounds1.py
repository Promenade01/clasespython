class animal:
    #constructor con parametros
    def __init__(self,nombre,raza,edad,peso):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso

    def comer(self):
        print(f"El animal {self.nombre} esta comiendo")

    def caminar(self):
        print(f"El animal de raza {self.raza} esta caminando")

    def dormir(self):
        print(f"El animal {self.nombre} esta dormiendo")
        
#Definir una instancia de tipo Animal para un objeto llamado perro
perro=animal("Brando","San Bernando",3,30)
#Definir una instancia de tipo Animal para un objeto llamado gato
gato=animal("Roll","Persa",4,3)

#setear valores a los atributos
perro.nombre="Bob"

perro.caminar()
perro.comer()
perro.dormir()

gato.caminar()
gato.comer()
gato.dormir()

#realizar 5 instancias de diferentes tipos de animales, modificar y asignar sus valores a los atributos