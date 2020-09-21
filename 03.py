def maior_e_men(cont):
    maior = 0
    menor = 0

    while True:
        num = int(input())     
        cont +=1

        if num == 0: break

        if cont ==1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

    return maior, menor

def main():
    cont = 0       
    maxi, mnr = maior_e_men(cont)

    if maxi != 0 and mnr != 0:
        print(f'{maxi}{mnr}')

if __name__ == '__main__':
    main() 
