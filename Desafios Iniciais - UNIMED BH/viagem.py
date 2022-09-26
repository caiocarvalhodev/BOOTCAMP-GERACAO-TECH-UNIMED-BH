valores = input().split() 

horas = int(valores[0])
velocidade = int(valores[1])

litros = velocidade / 12
media = horas*litros

print(f"{media:3.3f}")