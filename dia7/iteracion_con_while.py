#Contando con WHILE

contar = 0
while contar < 10:
    print("Esto se mostrará 10 veces")
    contar = contar + 1 #contar +=1 --> es lo mismo.
print("Fin de programa")

#Sumando de 1 a 100
i = 1
suma = 0

while i <= 100:
    suma += i
    i += 1
    print(f"suma temporal es: {suma}")

print(f"Resultado final es {suma}")
