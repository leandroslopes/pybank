class AtualizadorDeContas:
	
	def __init__(self, selic, saldo_total=0):
		self._selic = selic
		self._saldo_total = saldo_total
	
	@property
	def selic(self):
		return self._selic
		
	@property
	def saldo_total(self):
		return self._saldo_total
	
	def roda(self, conta):
		print('\nSaldo anterior: {}'.format(conta.saldo))
		conta.atualiza(self.selic)
		print('Saldo atual: {}'.format(conta.saldo))
		self._saldo_total += conta.saldo