## Calculadora de dois numeros
n1,n2 = input("Digite dois números: ").split()
n1 = int(n1)
n2 = int(n2)

print(f"A soma dos números é: {n1+n2}")
print(f"A subtração dos números é: {n1-n2}")
print(f"A multiplicação dos números é: {n1*n2}")
print(f"A divisão dos números é: {n1/n2}")

### Circulo
raio = int(input("Digite o raio do círculo: "))
area = 3.14*(raio**2)
circ = 2*3.14*raio

print(f"A área é: {area} e a circunferência é: {circ}")