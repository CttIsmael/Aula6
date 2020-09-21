def anos(deposito, taxa):
    anos = 0
    dobro = deposito * 2
    while deposito < dobro:
        juros = (taxa/100) * deposito
        deposito += juros
        anos += 1
    return anos

def main():
    deposito = float(input())
    taxa = float(input())
    print(anos(deposito,taxa))

if __name__ == "__main__":
    main()
