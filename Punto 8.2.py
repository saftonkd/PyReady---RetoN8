def cuadrados(*args)-> list: # Función 1 de 3
    lista_cuadrados : list = [x**2 for x in args] # Calcula los cuadrados de los enteros de la lista de entrada
    return lista_cuadrados

def pares_impares(*args)-> list: # Función 2 de 3
    for z in args:
      pares = [x for x in range(z + 1) if x % 2 == 0] # Indexa a la lista el elemento si cumple ser par
      impares = [x for x in range(z + 1) if x % 2 != 0] # Indexa a la lista el elemento si cumple ser impar
      return pares, impares

def divisores(*args)-> list: # Función 3 de 3
   return {n: [x for x in range(1, n + 1) if n % x == 0] for n in args} # Calcula los divisores de los argumentos y los retorna en estructura de Diccionario

if __name__ == "__main__":
  print("Función 1: Cuadrado de números") # Función 1 de 3
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  c = int(input("Ingrese numero c: "))
  d = int(input("Ingrese numero d: "))
  print(cuadrados(a, b, c, d))

  print("Función 2: Pares e Impares") # Función 2 de 3
  valor_primero = int(input("Ingrese un primer valor: ")) 
  valor_segundo = int(input("Ingrese un segundo valor: "))
  pares, impares = pares_impares(valor_primero, valor_segundo)
  print("Pares del primer valor:", pares) 
  print("Impares del primer valor:", impares)
  print("Pares del segundo valor:", pares) 
  print("Impares del segundo valor:", impares)

  print("Función 3: Divisores") # Función 3 de 3
  e = int(input("Ingrese un primer entero para calcular sus divisores: "))
  f = int(input("Ingrese un segundo entero para calcular sus divisores: "))
  print(divisores(e, f))


