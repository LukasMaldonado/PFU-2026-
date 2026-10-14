#Ejercicio 86: Leer 10 números y determinar cuántos son pares y cuántos impares. Usa: Para + Si.

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("no podes meter eso pe.")


class ContadorParesImpares:
    def __init__(self, cantidad=10):
        self.cantidad = cantidad
        self.pares = 0
        self.impares = 0

    def leer_numeros(self):
        for i in range(1, self.cantidad + 1):
            numero = leer_entero(f"Número {i}: ")
            if numero % 2 == 0:
                self.pares += 1
            else:
                self.impares += 1

    def mostrar_resultado(self):
        print("Pares: ",self.pares)
        print("Impares: ",self.impares)


if __name__ == "__main__":
    contador = ContadorParesImpares()
    contador.leer_numeros()
    contador.mostrar_resultado()
