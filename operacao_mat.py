# Vamos solicitar como entrada dois números inteiros e realizar as operações matemáticas de soma, subtração, multiplicação e divisão entre eles. Ao final, exibiremos o resultado de cada operação.

# Solicitando ao usuário que digite dois números inteiros

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Realizando as operações matemáticas
operação = input("Digite a operação desejada: (+, -, *, /)")

if operação == "+":
    resultado = numero1 + numero2
elif operação == "-":
    resultado = numero1 - numero2
elif operação == "*":
    resultado = numero1 * numero2
elif operação == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operação inválida"

if isinstance(resultado, (int, float)) and resultado < 0:
    resultado = abs(resultado)

print(resultado)
    