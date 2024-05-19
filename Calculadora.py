def Sumar(a,b):
    return a + b

def Restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    if b == 0:
        return 'No se puede  dividir el 0'
    return a / b

def MostrarMenu():
    
    print(f'---CALCULADORA---',
          f'\n1.Sumar.',
          f'\n2.Restar.',
          f'\n3.Multiplicar.'
          f'\n4.Dividir.',
          f'\n5.Salir.')
    

def ElegirOpcion():
    while True:
        try:
            opcion = int(input('Elige una opción: '))

            if 1 <= opcion <= 5:
                return opcion
            else:
                print('Eliga una opción válida..')
        except ValueError:
            print('Error de ingreso de datos, ingrese un número.')

def ObtenerNumero(prompt):
    while True:
        try:
            numero = float(input(prompt))

            return numero
        except ValueError:
            print('Error de ingreso de datos, ingrese un número.')
def main():
    while True:
        MostrarMenu()
        opcion = ElegirOpcion()

        if opcion == 5:
            print('Has salido de la calculadora.')
            break 

        numero1 = ObtenerNumero('Ingrese el primer número: ')
        numero2 = ObtenerNumero('Ingrese el segundo número: ')

        if opcion == 1:
            resultado = Sumar(numero1, numero2)
        elif opcion == 2:
            resultado = Restar(numero1, numero2)
        elif opcion == 3:
            resultado = Multiplicar(numero1, numero2) 
        elif opcion == 4:
            resultado = Dividir(numero1, numero2)
       
        print(f'El resultado es: {resultado}')


if __name__ == '__main__':
    main()
