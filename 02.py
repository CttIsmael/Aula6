def nao_zero(soma, cont):
    if soma > 0:
       media = soma/cont
       print(f'{media:.2f}')

def main():
    soma = 0
    cont = 0
    while True:
        num = int(input())
        soma = soma + num
        cont +=1
        if num == 0: 
            cont -=1
            break
    nao_zero(soma, cont)   


if __name__ == '__main__':
    main() 
