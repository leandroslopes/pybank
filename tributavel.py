import abc

class Tributavel(abc.ABC):
	""" Classe que contem operacoes de um objeto autenticavel
	As subclasses concretas devem sobrescrever o método get_valor_imposto.
	"""
	
	@abc.abstractmethod
	def get_valor_imposto(self):
		""" Aplica taxa de imposto sobre um determinado valor do objeto """
		pass