def potencia(exponente : float, base : int) -> float:
  if exponente == 0: # Caso base
      return 1
  elif exponente < 0:
      return 1 / potencia(-exponente, base) # Reescribir el exponente negativo aplicando la propiedad matemática
  else:
      return base * potencia(exponente -1, base) # Multiplicar la base exponente veces hasta que exponente == 0

if __name__ == "__main__":
  a = int(input("Ingrese el primer exponente de prueba: "))
  b = int(input("Ingrese la primera base de prueba: "))
  print(potencia(a, b))
  c = int(input("Ingrese el segundo exponente de prueba: "))
  d = int(input("Ingrese la segunda base de prueba: "))
  print(potencia(c, d)) 

