from collections.abc import MutableSequence
from conta import Conta

class Contas(MutableSequence):
	
	_dados = []
	
	def __len__(self):
		return len(self._dados)
		
	def __getitem__(self, posicao):
		return self._dados[posicao]
		
	def __setitem__(self, posicao, valor):
		if (isinstance(valor, Conta)):
			self._dados[posicao] = valor
		else:
			raise ValueError("Valor atribuido nao eh uma conta")
		
	def __delitem__(self, posicao):
		del self._dados[posicao]
		
	def insert(self, posicao, valor):
		if (isinstance(valor, Conta)):
			return self._dados.insert(posicao, valor)
		else:
			raise ValueError('Valor inserido nao eh uma conta')

if __name__ == '__main__':
	import csv
	from conta import ContaCorrente
	
	contas = Contas()
	arquivo = open('contas.txt', 'r')
	leitor = csv.reader(arquivo)
	
	for linha in leitor:
		conta = ContaCorrente(linha[0], linha[1], float(linha[2]))
		contas.append(conta)
	
	print('Saldo Anterior - Imposto - Saldo Atualizado')
	for c in contas:
		saldo_anterior = c.saldo
		c.saca(c.get_valor_imposto())
		c.atualiza(0.01)
		saldo_atual = c.saldo
		print('{} - {} - {}'.format(saldo_anterior, c.get_valor_imposto(), saldo_atual))
		
	arquivo.close()