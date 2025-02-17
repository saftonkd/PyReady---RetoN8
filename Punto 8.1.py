if __name__ == "__main__":
  print("Función 1: Cuadrado de números") # Función 1 de 3
  a = int(input("Ingrese el valor máximo de la lista para calcular: "))
  numeros = range(1, a + 1)
  cuadrados = (lambda lista: [x**2 for x in lista])(numeros) # Calcula el cuadrado de cada entero de la lista
  print(cuadrados)

  print("Funcion 2: Pares e Impares") # Función 2 de 3
  b = int(input("Ingrese el valor máximo de la lista: "))
  pares_impares = lambda z: ([x for x in range(z + 1) if x % 2 == 0], [x for x in range(z + 1) if x % 2 != 0]) # Distribuye a cada entero de la lista en dos listas diferentes dependiendo si es par o impar
  pares, impares = pares_impares(b)
  print("Pares:", pares)   
  print("Impares:", impares)

  print("Función 3: Divisores:") # Función 3 de 3
  c = int(input("Ingrese un entero para calcular sus divisores: "))
  divisores = lambda n: [x for x in range(1, n + 1) if n % x == 0] # Calcula los divisores del entero de entrada
  print(divisores(c))

