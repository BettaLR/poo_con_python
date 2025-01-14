class Personaje:
    #Atributos de la clase
    nombre = 'default'
    fuerza = 0
    inteligencia = 0 
    defensa = 0
    vida = 0
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre     #El signo de igual es una asignasion
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre)
        print("-Fuerza: ", self.fuerza)
        print("-Inteligencia: ", self.inteligencia)
        print("-Defensa: ", self.defensa)
        print("-Vida: ", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, " puntos de daño a ", enemigo.nombre)
        print("Vida de ", enemigo.nombre, " es", enemigo.vida)

#Variable del constructor de la clase
mi_personaje = Personaje("Trakalosa de monterrey", 70, 90, 50, 100)
mi_enemigo = Personaje("La arrolladora banda limón", 60, 90, 40, 100)
#print (mi_personaje.esta_vivo())
#print (mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.dañar(mi_enemigo))
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
