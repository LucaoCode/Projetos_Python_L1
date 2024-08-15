# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente
class ContaCorrente():
# Atributos: numero da conta, nome do titular e saldo
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

# Métodos: alterar nome, deposito e saque
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado {valor} na conta de {self.nome}. Saldo atual: {self.saldo}')

    def mostrarSaldo(self):
        return f"Seu saldo atual é{self.saldo}"
# construtor: saldo é opcional com o valor inicial igual a 0

# instanciar
lucas = ContaCorrente(1,"Lucas")
lucas.depositar(200)
print(lucas.mostrarSaldo()) #