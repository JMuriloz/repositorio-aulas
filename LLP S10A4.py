def caixa_eletronico(valor_saque):
    notas = [50, 20, 10, 5]
    qtd_notas = [0, 0, 0, 0]  # quantidade de cada nota inicialmente é zero
    total = valor_saque

    for i in range(len(notas)):
        while total >= notas[i]:
            total -= notas[i]
            qtd_notas[i] += 1

    return qtd_notas

def main():
    valor_saque = float(input("Digite o valor que deseja sacar: "))

    if valor_saque <= 0 or valor_saque % 5 != 0:
        print("Valor inválido! O valor do saque deve ser múltiplo de 5 e maior que zero.")
        return

    qtd_notas = caixa_eletronico(valor_saque)
    print("Quantidade de notas de R$ 50:", qtd_notas[0])
    print("Quantidade de notas de R$ 20:", qtd_notas[1])
    print("Quantidade de notas de R$ 10:", qtd_notas[2])
    print("Quantidade de notas de R$ 5:", qtd_notas[3])

if __name__ == "__main__":
    main()
