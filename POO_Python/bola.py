# Classe Bola: Crie uma classe que modele uma bola
# Atributos: Cor,circuferencia, material
# metodos: trocaCor e mostrar cor


class Bola():
    # Construtor da classe  ---------------------------
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

        # Metodos da classe ---------------------------
    def trocaCor(self,novaCor):
        self.cor = novaCor
    def trocaMaterial(self,novaMaterial):
        self.material = novaMaterial
    def mostrarCor(self):
        return self.cor
    def mostraMaterial(self):
        return self.material
    
    # Criando o objeto em string -----------------------
    def __str__(self):
        return f'Cor: {self.cor}, Circuferência: {self.circuferencia}cm, Material: {self.material}'

# instanciando classe 
jabulani = Bola('azul',3,'couro')
print (jabulani)

# chamando o metodo
jabulani.trocaCor('verde')
print (jabulani.mostrarCor())

jabulani.trocaMaterial('plástico')
print(jabulani.mostraMaterial())