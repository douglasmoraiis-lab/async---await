#Imprima apenas os números pares de 1 a 20.

multiplos_pares = []
for i in range(1, 21):
  if i % 2 == 0:
    multiplos_pares.append(i)
  print(multiplos_pares)