# Una funcion que capture los valores enunciados y de acuerdo a la periosidad en meses, agregue o descuente intereses, si el tiempo es menor a 2, castiga al cliente con 2% de descuento, si es mayor
# de da beneficios de 3%
usuario= input('Digite el nombre de paciente    ')
capital= int(input('Digite el el valor del CDT : '))
tiempo= int(input('Digite la cantidad de meses : '))
Porcentaje_Interes=0.03


def CDT(usuario:str,capital:int,tiempo:int):
    POCENTAJE_PERDER= 0.02
    PPORCENTAJE_GANAR= 0.03
    if (tiempo<=2):
        Valor_Aperder=capital*POCENTAJE_PERDER
        Valor_Total= capital - Valor_Aperder
       
        
    else:
        Valor_Interes = ((capital * PPORCENTAJE_GANAR * tiempo)/12)
        Valor_Total = float(Valor_Interes + capital)
           
    return 'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'
print(CDT(usuario, capital, tiempo))
