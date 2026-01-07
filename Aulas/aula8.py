#operadores lógicos - o resultado é um booleano
# or / and / not

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp2 = saldo >= saque and saque <= limite or (conta_especial and saldo >= saque)
print(exp2)