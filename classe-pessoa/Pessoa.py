class Pessoa:
    pessoas = []
    def __init__(self,nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        print(f'{self._nome.ljust(25)} | {self._idade.ljust(25)} | {self._profissao}' )
    
    def aniversario(self):
        self._idade = + 1
    
    @property
    def saudacao(self):
        print(f'Me chamo {self._nome} tenho {self._nome} anos e trabalho como {self._profissao}')

    
jozildo = Pessoa('Jozildo Freitas', '45', 'Pedreiro')
jozildo.saudacao

