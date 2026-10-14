#Ejercicio 94: Registrar edades hasta ingresar 0 y determinar la cantidadde mayores y menores de edad.Usa: Mientras + Si.


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("pone otro numero papi")

class RegistroEdades:
    MAYORIA_EDAD = 18

    def __init__(self):
        self.mayores = 0
        self.menores = 0

    def leer_edades(self):
        edad = leer_entero("Edad (0 para terminar): ")
        while edad != 0:
            if edad < 0:
                print("La edad no puede ser negativa.")
            elif edad > 100:
                print("se pasa de la edad maxima.")
            elif edad >= self.MAYORIA_EDAD:
                self.mayores += 1
            else:
                self.menores += 1
            edad = leer_entero("Edad (0 para terminar): ")

    def mostrar_resultado(self):
        print("Mayores de edad: ",self.mayores)
        print("Menores de edad: ",self.menores)


if __name__ == "__main__":
    registro = RegistroEdades()
    registro.leer_edades()
    registro.mostrar_resultado()
