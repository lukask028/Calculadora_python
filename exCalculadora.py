"""Calculadora com while """
soma = lambda n1, n2 : n1 + n2
subtracao = lambda n1, n2 : n1 - n2 
multiplicacao = lambda n1, n2 : n1 * n2
divisao = lambda n1, n2 : n1 / n2 
while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro número: ')
    operador = input('digite o operador (+-/*): ')
    
    numeros_validos = None
    
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(numero_1)
        n2_float = float(numero_2)
        numeros_validos = True
    except:
        
        print('error')
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos dos números não são válidos')
            continue
        
        
    operadores_permitidos = ('+', '-', '/', '*')
       
    if len(operador) > 1:
           print("Digite apenas um operador")
           continue
       
    if operador not in operadores_permitidos:
           print("Operador inválido")
           continue
       
       
    if operador == '+' :
          
           print(f'{n1_float}' '+' f'{n2_float}=', round(soma(n1_float,n2_float),2))
        
    elif operador == '-' :
    
            print(f'{n1_float}' '-' f'{n2_float}=', round(subtracao(n1_float,n2_float),2))
           
    elif operador == '*' :
            print(f'{n1_float}' '*' f'{n2_float}=', round(multiplicacao(n1_float,n2_float),2))
           
    elif operador == '/' :
            print(f'{n1_float}' '/' f'{n2_float}=', round(divisao(n1_float,n2_float),2))
           
    else:
            print('operadores inválidos')
       
    sair = input('Quer sair? [s]Sim: ').lower().startswith('s')

    
    if sair is True: 
        break