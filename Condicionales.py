
# Programa que suma todos 
# los numeros que ingresamos

while True:

	try:
		total = 0

		# Numeros

		suma = input('Numeros sepadaros por espacios: ')
		suma = suma.split()

		"""
		Bucle que evalua si el dato 
		es un numero y al serlo los 
		guarda en la variable total
		"""

		for numero in suma:
			if numero.isnumeric():
				total += float(numero)

			else:
				raise ValueError('No es un numero')

	# Excepciones que manejan los errores de ejecucion

	except ValueError:
		print('Son incorrectos')
		print('Vuelve a introducir los numeros')

	else:		
		print(f'El valor de la suma: {total}')
		break

	finally:
		print('Ha terminado la iteracion')