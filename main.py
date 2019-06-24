from conta import Conta
from cliente import Cliente

cliente = Cliente('Leandro', 'Lopes', '00336077378')
conta = Conta(123, cliente, 100, 1000)

cliente1 = Cliente('Kerly', 'Lopes', 123456)
conta1 = Conta(321, cliente1, 200, 1000)

conta.deposita(100)
conta.saca(50)
conta.transfere_para(conta1, 20)
conta.extrato()
conta.historico.imprime()
print(conta)

conta1.extrato()
conta1.historico.imprime()
print(conta1)