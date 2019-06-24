
def criar_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta 

def deposito(conta, valor):
    conta['saldo'] += valor
    
def saca(conta, valor):
    conta['saldo'] -= valor

def	extrato(conta):
    	print("Numero: {} \nSaldo: {}".format(conta['numero'],	 conta['saldo']))