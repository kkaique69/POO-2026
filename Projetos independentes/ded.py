import random
class Personagem:
    def __init__(self, nome:str, idade:int, classe:str, raca:str) -> None:
        self.nome = nome;
        self.idade = idade;
        self.classe = classe;
        self.raca = raca;
        self.atributos = [];

    def addAtributos(self) -> None:
        for j in range(6):
            self.puro = [];
            for i in range(4):
                dado = random.randint(1, 6);
                self.puro.append(dado);
                self.puro = sorted(self.puro);
            self.puro.pop(0)
            self.atributos.append(sum(self.puro))
        print(self.atributos)

kahh = Personagem("Kahh", 23, "Guerreiro", "Dragonato");
print(kahh.nome)
print(kahh.idade)
print(kahh.classe)
print(kahh.raca)
kahh.addAtributos()