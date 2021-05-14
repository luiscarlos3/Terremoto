import math
from write import Console
amplitud =  Console.inputDecimal("ingrese la amplitud : ") 
diferencia = Console.inputDecimal("Ingrese la diferencia de ondas superficiales y ondas profundas : ") 
def calcular(amplitud, diferencia):
    magitud =0    
    num1 = math.log10(amplitud)
    num2 = 8 * diferencia
    num3 = 3 * math.log10(num2)
    magitud = num1 + (num3 - 2.92)    
    return magitud
print("El es de sismo magnitud ","{:.3f}".format(calcular(amplitud, diferencia)))
def escala(num):
    value = math.floor(num)
    print("Escala de ritcher Magnitud : ", value)
    if value <= 3.5:
        print("Microsismo detectado por instrumentos")
    elif value >= 3.5 and value <= 5.4:
        print("Sentido por algunas personas (generalmente en reposo)")
    elif value >= 5.5 and  value <= 6.0:
        print("Sentido por algunas personas dentro de edificios")
    elif value >= 6.1 and value <= 6.9:
        print("Sentido por algunas personas fuera del edificios")
    elif value >= 7.0 and value <= 7.9:
        print("sentido por casi todos ")
    elif value >= 8:
        print("destructivo")
   
   
escala(calcular(amplitud, diferencia))
