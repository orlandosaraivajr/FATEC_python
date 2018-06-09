#valor_recebido = float(input("Digite o valor pago: "))
#valor_compra = float()

def troco(valor_recebido, valor_compra):
	valor_troco = valor_recebido - valor_compra					
	
	qnt_100 = valor_troco // 100
	valor_troco = valor_troco % 100
	qnt_50 = valor_troco // 50
	valor_troco = valor_troco % 50
	qnt_10 = valor_troco // 10
	valor_troco = valor_troco % 10
	qnt_5 = valor_troco // 5
	valor_troco = valor_troco % 5
	qnt_1 = valor_troco // 1
	valor_troco = valor_troco % 1

	qnt_050 = valor_troco // 0.50
	valor_troco = valor_troco % 0.50
	qnt_010 = valor_troco // 0.10
	valor_troco = valor_troco % 0.10
	qnt_005 = valor_troco // 0.05
	valor_troco = valor_troco % 0.05
	qnt_001 = valor_troco // 0.01
	valor_troco = valor_troco % 0.01

	return [[qnt_100, qnt_50, qnt_10, qnt_5, qnt_1], [qnt_050, qnt_010, qnt_005, qnt_001]]


assert(troco(100, 48) == [[0,1,0,0,2],[0,0,0,0]])
assert(troco(95, 50) == [[0,0,4,1,0],[0,0,0,0]])
#assert(troco(valor_recebido, 48) == [[0,1,0,0,2],[0,0,0,0]])
assert(troco(10.5, 8.95) == [[0,0,0,0,1],[1,0,1,0]])
assert(troco(1	50, 140) == [[0,0,1,0,0],[0,0,0,0]])
assert(troco(140, 150) == [[0,0,1,0,0],[0,0,0,0]])
