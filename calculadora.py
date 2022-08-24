def calculadora(num_1, num_2, operacao):

    num_1 = float(num_1)
    num_2 = float(num_2)
    operacao = str(operacao)
    resultado = ''

    if operacao == 'multiplicacao':
        resultado = num_1 * num_2
    elif operacao == 'divisao':
        if num_2 == 0.0:
            #print('\n----------------------------------------\n')
            #print('Não é possível dividir um número por 0.')
            #print('\n----------------------------------------\n')
            resultado = 'Não é possível dividir um número por 0.'
        else:
            resultado = num_1 / num_2
    elif operacao == 'adicao':
        resultado = num_1 + num_2
    elif operacao == 'subtracao':
        resultado = num_1 - num_2
    else:
        #print('\n----------------------------------------\n')
        #print('Não é uma operação válida')
        #print('\n----------------------------------------\n')
        resultado = 'Não é uma operação válida.'

    return resultado


#print(calculadora(2, 2, 'multiplicacao'))
#print(calculadora(2, 2, 'divisao'))
#print(calculadora(2, 0, 'divisao'))
#print(calculadora(2, 2, 'adicao'))
#print(calculadora(2, 2, 'subtracao'))