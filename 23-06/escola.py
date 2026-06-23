from datetime import date

class Presenca:
    def __init__(self, ID:int, data:str) -> None:
        self.ID = ID;
        self.data = data;

class Pessoa:
    def __init__(self, CPF:str, nome:str) -> None:
        self.CPF = CPF;
        self.nome = nome;
        self.listaFrequencia = [];
        
    def addPresenca(self, ID:int, data:date) -> None:
        self;listaPresenca.append(Presenca(ID, data));

class Docente(Pessoa):
    def __init__(self, CPF:str, nome:str, salario:float) -> None:
        super().__init__(CPF, nome);
        self.salario = salario;

class Atividade:
    def __init__(self, codigo:int, descricao:str, valor:float) -> None:
        self.codigo = codigo;
        self.descricao = descricao;
        self.valor = valor;

class Estudante(Pessoa):
    def __init__(self, CPF:str, nome:str, RA:str) -> None:
        super().__init__(CPF, nome);
        self.RA = RA;
        listaAtividade = [];

    def addAtividade(self, atv:Atividade) -> None:
        self.listaAtividade.append(atv);
