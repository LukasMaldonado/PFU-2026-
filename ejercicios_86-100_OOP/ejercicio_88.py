#Ejercicio 88: Leer N números y calcular suma y promedio. Usa: Para + acumulador.


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser mayor que 0 puesh")
        except ValueError:
            print("no sirve, tiene ke ser valido.")


def leer_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("no sirve, pon otro numero")


class SumaPromedio:
    def __init__(self, n):
        self.n = n
        self.suma = 0

    def leer_numeros(self):
        for i in range(1, self.n + 1):
            self.suma += leer_numero(f"Número {i}: ")

    def promedio(self):
        return self.suma / self.n

    def mostrar_resultado(self):
        print(f"Suma: {self.suma}")
        print(f"Promedio: {self.promedio():.2f}")


if __name__ == "__main__":
    n = leer_entero_positivo("¿Cuántos números quieres ingresar? ")
    app = SumaPromedio(n)
    app.leer_numeros()
    app.mostrar_resultado()
