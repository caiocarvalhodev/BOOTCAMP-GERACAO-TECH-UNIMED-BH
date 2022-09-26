
entrada = input().split()
distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

resultado = (distancia/(diametro1 + diametro2))
icm = resultado

print(f'{icm:2.2f}')
