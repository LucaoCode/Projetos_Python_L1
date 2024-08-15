class Carro():
    def __init__(self, consumo): # construtor
        # Atributos de Carro
        self.consumo = consumo
        self.nivelCombustivel = 0

    # Metodos
    def obterGasolina(self):
        return self.nivelCombustivel
    def adicionarGasolina(self, gasolina):
        self.nivelCombustivel += gasolina
        if self.nivelCombustivel > 100:
            self.nivelCombustivel = 100
            print("Carro cheio!")
    def andar(self, km):
        consumo = km/self.consumo
        self.nivelCombustivel -= self.nivelCombustivel

# instancia do objeto

meuSedan = Carro(10)
meuSedan.adicionarGasolina(50)
print(meuSedan.obterGasolina())

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
print (meuFusca.obterGasolina())
