
def Division(A, B):

	try:
		print(f"Resultado: {A / B}")

	except ZeroDivisionError:
		print("No se puede dividir por cero")

Division(2, 0)