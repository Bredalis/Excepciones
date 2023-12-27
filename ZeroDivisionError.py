
def division(a, b):

	try:
		print(f'Resultado: {a / b}')

	except ZeroDivisionError:
		print('No se puede dividir por cero')

division(2, 0)