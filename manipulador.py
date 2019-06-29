class ManipuladorDeTributaveis:
	
	def calcula_impostos(self, lista_tributaveis):
		total = 0
		for t in lista_tributaveis:
			if (isinstance(t, Tributavel)):
				total += t.get_valor_imposto()
			else:
				print(t.__repr__(), " nao	eh	um	tributavel")
		return total

if __name__ == '__main__':
	from conta import ContaCorrente, ContaInvestimento, SeguroDeVida
	from tributavel import Tributavel
	
	cc1 = ContaCorrente('123-4', 'João', 1000.0)
	cc2 = ContaCorrente('123-5', 'José', 1000.0)
	
	ci1 = ContaInvestimento('123-6', 'Maria', 2000.0)
	
	seguro1 = SeguroDeVida(100.0, 'José', '345-77')	
	seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')
	
	Tributavel.register(ContaCorrente)
	Tributavel.register(ContaInvestimento)
	Tributavel.register(SeguroDeVida)
	
	lista_tributaveis = []	
	lista_tributaveis.append(cc1)	
	lista_tributaveis.append(cc2)
	lista_tributaveis.append(ci1)	
	lista_tributaveis.append(seguro1)
	lista_tributaveis.append(seguro2)
	
	manipulador = ManipuladorDeTributaveis()
	total = manipulador.calcula_impostos(lista_tributaveis)
	print(total)