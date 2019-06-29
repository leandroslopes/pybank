from historico import Historico
from data import Data
from atualizador_de_contas import AtualizadorDeContas
from banco import Banco
import abc
from tributavel import Tributavel

class Conta(abc.ABC):
	
	__slots__ = {'_numero', '_titular', '_saldo', '_limite', '_historico', '_data_abertura'}
	_identificador = 0
	
	def __init__(self, numero, cliente, saldo=0, limite=1000.0):
		self._numero = numero
		self._titular = cliente
		self._saldo = saldo
		self._limite = limite
		self._historico = Historico()
		self._data_abertura = Data()
		self._tipo = type(self).__name__
		Conta._identificador += 1
	
	@property		
	def saldo(self):
		return self._saldo
		
	@property		
	def numero(self):
		return self._numero
		
	@property		
	def titular(self):
		return self._titular
		
	@property		
	def historico(self):
		return self._historico
		
	@property		
	def data_abertura(self):
		return self._data_abertura
	
	@property		
	def limite(self):
		return self._limite
		
	@staticmethod		
	def get_identificador():
		return Conta._identificador
    
	def deposita(self, valor):
		if (valor < 0):
			raise ValueError('Voce tentou depositar um valor negativo')
		else:
			self._saldo += valor
			self.historico.transacoes.append("Deposito de {}".format(valor))
        
	def saca(self, valor):
		if (valor < 0):
			raise ValueError('Voce tentou sacar um valor negativo')
		if (self._saldo < valor):
			raise SaldoInsuficienteError()
		self._saldo -= (valor + 0.10)
		self.historico.transacoes.append("Saque de {}".format(valor))
		return True

	def transfere_para(self, destino, valor):
		retirou = self.saca(valor)
		if (retirou == False):
			return False
		else:
			destino.deposita(valor)
			self.historico.transacoes.append("Transferencia de {} para conta {}".format(valor, destino.numero))
			return True
        
	def extrato(self):
		print('\nIdentificador: {}\nCliente: {} \nNumero: {} \nSaldo: {}'.format(self.get_identificador(), self.titular.nome, self.numero, self.saldo))
		print("Data abertura: {}/{}/{}".format(self.data_abertura.dia, self.data_abertura.mes, self.data_abertura.ano))
		self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))
	
	@abc.abstractmethod
	def atualiza():
		pass
	
	@property	
	def tipo(self):
		return self._tipo

	def __str__(self):
		str = '\nCliente: {} \nNumero: {} \nSaldo: {}\nLimite: {}'.format(self.titular.nome, self.numero, self.saldo, self.limite)
		str += '\nData abertura: {}/{}/{}'.format(self.data_abertura.dia, self.data_abertura.mes, self.data_abertura.ano)
		return str

class TributavelMixIn:
	
	def get_valor_imposto(self):
		pass

class ContaCorrente(Conta):
	
	def atualiza(self, taxa):
		self._saldo += self._saldo * taxa * 2
		
	def deposita(self, valor):
		self._saldo += valor - 0.10
	
	def get_valor_imposto(self):
		return self._saldo * 0.01
	
class ContaPoupanca(Conta):
	
	def atualiza(self, taxa):
		self._saldo += self._saldo * taxa * 3

class ContaInvestimento(Conta):
	
	def atualiza(self, taxa):
		self._saldo += self._saldo * taxa * 5
	
	def get_valor_imposto(self):
		return self._saldo * 0.03

class SeguroDeVida():
	
	def __init__(self, valor, titular, numero_apolice):
		self._valor = valor
		self._titular = titular
		self._numero_apolice = numero_apolice

	def get_valor_imposto(self):
		return 50 + self._valor * 0.05

class SaldoInsuficienteError(RuntimeError):
	pass

if __name__ == '__main__':
	b = Banco()
	cc = ContaCorrente('123-5', 'Jose', 1000.0)
	cp = ContaPoupanca('123-6', 'Maria', 1000.0)
	ci = ContaInvestimento('123-7', 'Antonia', 1000.0)
	
	b.adiciona(cc)
	b.adiciona(cp)
	b.adiciona(ci)
	
	adc = AtualizadorDeContas(0.01)
	for conta in b.get_contas:
		adc.roda(conta)
		print(conta.tipo)
	
	print('\nSaldo total: {}'.format(adc.saldo_total))