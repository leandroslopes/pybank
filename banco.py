class Banco:
	
	def __init__(self):
		self.contas = []
	
	def adiciona(self, conta):
		self.contas.append(conta)
		
	def get_conta(self, posicao):
		return self.contas[posicao]
	
	def get_total_contas(self):
		return len(contas)
	
	@property
	def get_contas(self):
		return self.contas