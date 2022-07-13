
def calcular():
    operacao = input('''
Digite a operação matemática que deseja concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')
    numero_1 = int(input('Coloque o primeiro numero: '))
    numero_2 = int(input('Coloque o segundo numero: '))

    if operacao == '+':
#Adição
       print('{} + {} = '.format(numero_1, numero_2))#formatadores de string
       print (numero_1 + numero_2)

    elif operacao == '-':
#Subtração
        print('{} - {} = '.format(numero_1, numero_2))
        print (numero_1 - numero_2)

    elif operacao == '*': 
#Multiplicação
        print('{} * {} = '.format(numero_1, numero_2))
        print (numero_1 * numero_2)

    elif operacao == '/':
#Divisão
        print('{} / {} = '.format(numero_1, numero_2))
        print (numero_1 / numero_2)
    
    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

# Adiciona a função again() à função calcular()
    again()

# Defina a função again() para perguntar ao usuário se ele deseja usar a calculadora novamente
def again():
    
    # Recebe entrada do usuário
    calc_again = input('''
Deseja calcular novamente?
Digite Y para SIM ou N para NÃO.
   ''' )
    
    # Se o usuário digitar Y, execute a função calculate()
    if calc_again.upper() == 'Y':
        calcular()     
    # Se o usuário digitar N, diga adeus ao usuário e encerre o programa
    elif calc_again.upper == 'N':
        print ("ate mais tarde.")
    # Se o usuário digitar outra chave, execute a função novamente
    else:
        again()
        
calcular()

