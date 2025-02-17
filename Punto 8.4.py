import time

# Función recursiva para hallar los términos de la serie de Fibonacci
def fibonacci(n : int)-> int:
  if n <= 1:
      return n
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)

# Función para medir el tiempo de ejecución
def tiempo_ejecucion(fibonacci, n : int) -> float:
    tiempo_inicio = time.time()
    fibonacci(n)
    tiempo_fin = time.time()
    return tiempo_fin - tiempo_inicio

if __name__ == "__main__":
# Medir y comparar el tiempo de ejecución
  for n in range(0, 100):
    tiempo = tiempo_ejecucion(fibonacci, n)
    print(f"Fibonacci({n}) {tiempo:.6f} seconds")
    if tiempo > 10:  # Consideraremos una diferencia de 10 segundos como un tiempo significativo
        print(f"En Fibonacci({n}), la diferencia de tiempo es significativa.")
        break