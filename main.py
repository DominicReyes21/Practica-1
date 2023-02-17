print('\n\n')
print("xxxxxxxxxxxxxxxxx")
print("Calcular ISR")
print("xxxxxxxxxxxxxxxxx")
print('\n\n')
'''Primero lo que va a hacer mi codigo es preguntarle al usuario cuánto gana'''
a=(float(input("¿Cuanto gana al mes en bruto?:" )))
'''Despues le va a preguntar cuantos dependientes tiene'''
b=(int(input("¿Cuantos dependientes tiene?: ")))
'''Como nos piden que calculemos el impuesto anual vamos a multiplicar el resultado de la variable ISR
 por 12'''
'''Ahora vamos a hacer la formula para calcular el ISR'''
ISR=(a-2000*b)*12
'''Despues de que sacamos el ISR vamos a guardarlo en una nueva variable que en este caso seria ISR2
para asi poder sacar el 20 porciento '''
ISR2=ISR*20/100
'''Ahora en el ISR3 vamos a poner ese comando para que solo cuente los primeros 2 decimales'''
ISR3=round(ISR2, 2)
'''Por último ya le decimos al usuario cuanto debe de pagar de ISR'''
print("El total de ISR anualmente a pagar es:",ISR3)