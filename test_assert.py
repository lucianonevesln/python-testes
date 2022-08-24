from calculadora import calculadora

try:
    resultado = calculadora(10, 10, 'multiplicacao')
    assert resultado == 100.0
    print('OK!')
except AssertionError:
    print('Incorreto!')

try:
    resultado = calculadora(10, 10, 'divisao')
    assert resultado == 1
    print('OK!')
except AssertionError:
    print('Incorreto!')

try:
    resultado = calculadora(10, 10, 'adicao')
    assert resultado == 20.0
    print('OK!')
except AssertionError:
    print('Incorreto!')

try:
    resultado = calculadora(10, 10, 'subtracao')
    assert resultado == 0.0
    print('OK!')
except AssertionError:
    print('Incorreto!')

try:
    resultado = calculadora(10, 0, 'divisao')
    assert resultado == 'Não é possível dividir um número por 0.'
    print('OK!')
except AssertionError:
    print('Incorreto!')

try:
    resultado = calculadora(10, 2, 'multiplicação')
    assert resultado == 'Não é uma operação válida.'
    print('OK!')
except AssertionError:
    print('Incorreto!')