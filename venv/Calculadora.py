

def binario (resultado):
    return print("\nEl resultado es:",resultado,"\nEn Binario es:",format(resultado, '0b'))

def Operacion (calculo):
    if (calculo == "S"):
        print("Estas Sumando")
        n1 = int(input("Ingresa tu primer numero: "))
        n2 = int(input("Ingresa tu segundo numero: "))
        resultado = n1 + n2
        binario(resultado)

    if (calculo == "R"):
        print("Estas Restando")
        n1 = int(input("Ingresa tu primer numero: "))
        n2 = int(input("Ingresa tu segundo numero: "))
        resultado = n1 - n2
        binario(resultado)

    if (calculo == "M"):
        print("Estas Multiplicando")
        n1 = int(input("Ingresa tu primer numero: "))
        n2 = int(input("Ingresa tu segundo numero: "))
        resultado = n1 * n2
        binario(resultado)

    if (calculo == "D"):
        print("Estas Dividiendo")
        n1 = int(input("Ingresa tu primer numero: "))
        n2 = int(input("Ingresa tu segundo numero: "))
        resultado = n1 / n2
        binario(resultado)


encendido = 1

while (encendido == 1):
    Resultado = 0
    calculo = str(input("Elije la operacion que quieres hacer: \nS = Suma\nR = Resta\nM = Multiplicacion\nD = Division\n\n"))
    Operacion(calculo)
    encendido = int(input("\n\nQuieres hacer Otro Calculo? \nEscribe 1 para continuar y 0 para apagar la calculadora\n"))

print("Hasta Luego!")


