from conta import ContaCorrente

def metodo1():
	print('Inicio do metodo1')
	metodo2()
	print('Fim do metodo1')

def metodo2():
	print('Inicio do metodo2')
	cc = ContaCorrente('José', '123')
	
	try:
		for i in range(1,15):
			cc.deposita(i + 1000)
			print(cc.saldo)	
			if (i == 5):
				cc = None
	except:
		print('erro')
			
	print('Fim do metodo2')

if __name__ == '__main__':
	print('Inicio do main')
	metodo1()
	print('Fim do main')