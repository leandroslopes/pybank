from datetime import date

class Data:
	def __init__(self):
		d = date.today()
		self.dia = d.strftime('%d')
		self.mes = d.strftime('%m')
		self.ano = d.strftime('%Y')