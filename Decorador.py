import time, random

def calcular_tiempo(funcion):
    def wrapper(self):
        inicio = time.time()
        funcion(self)
        fin = time.time()
        tiempo = fin - inicio
        tiempos.append(tiempo)
    return wrapper

class Trabajador:
    @calcular_tiempo
    def trabajar(self):
        segundos = random.uniform(0, 1)
        print(f"Se trabajó durante {segundos:.2f} segundos")
        time.sleep(segundos)

trabajador = Trabajador()
tiempos = []
iteraciones = 5
for i in range(iteraciones):
    trabajador.trabajar()

promedio_tiempo = sum(tiempos) / iteraciones

print(f"El tiempo promedio es: {promedio_tiempo:.2f} segundos")