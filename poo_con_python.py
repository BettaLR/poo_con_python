class Personaje:
    #Atributos de la clase
    #nombre = 'default'
    #fuerza = 0
    #inteligencia = 0 
    #defensa = 0
    #vida = 0
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre     #El signo de igual es una asignasion
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def atributos(self):
        print(self.__nombre)
        print("-Fuerza: ", self.__fuerza)
        print("-Inteligencia: ", self.__inteligencia)
        print("-Defensa: ", self.__defensa)
        print("-Vida: ", self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
     
    def esta_vivo(self):
        return self.__vida > 0 
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
    
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, " puntos de daño a ", enemigo.__nombre)
        if not enemigo.esta_vivo():
            enemigo.__morir()
        print("Vida de ", enemigo.__nombre, " es", enemigo.__vida)

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("ERROR")
        else:
            self.__fuerza = fuerza
        self.__fuerza = fuerza

#Variable del constructor de la clase
mi_personaje = Personaje("Trakalosa de monterrey", 8000, 90, 50, 100)
mi_enemigo = Personaje("La arrolladora banda limón", 60, 90, 40, 100)

#Prueba 1. Sin acceso al atributo fuerza
#print(mi_personaje.fuerza)
#mi_personaje.atributos()

#Prueba 2. Acceso morir
#mi_personaje.atacar(mi_enemigo)

#Prueba 3. Getters and setters
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(-100)
#print(mi_personaje.get_fuerza())
#mi_personaje.__Personaje__fuerza = 10
mi_personaje.set_fuerza(-100)
mi_personaje.atributos()