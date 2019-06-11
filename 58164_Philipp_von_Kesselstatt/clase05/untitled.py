
from calculadora_dificil import calculadora

calc = calculadora()

x = ''

for num in range(5):

    x = input('ingrese      ')

    calc.ingresar(x)

    print(calc.display())

    for l in range(len(calc.listan)):
        print(calc.listan[l])

print(calc.display())