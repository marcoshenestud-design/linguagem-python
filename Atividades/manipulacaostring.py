entrada = input('Digite os valores: ').strip()
saldo = 0.0

lancamentos = entrada.split(',')

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)

    if tipo == 'R':      
        saldo += valor
    elif tipo == 'D':    # Despesa
        saldo -= valor

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")
