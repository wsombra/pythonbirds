
class Pessoa:
    olhos = 2
    ''' 
    - Atributo de "classe", pois é um atributo comum entre os demais objetos (essa é a crítica)
    - Para criar os atributos utilizo o método especial __init_(self)
    - * QTD não definida |  parametros'''
    def __init__(self, *filhos,  nome=None, idade=40):
        # Atributos
        self.idade = idade
        self.nome  = nome
        # Atibuto filho recebe um list
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    '''
    Método de classe , iniciado com @, temos dois tipos : static e o class
    Exemplos:
    '''
    @staticmethod
    def calcula_imc():
        return 10

    ''' Ter acesso a classe que está executando o método'''
    @classmethod
    def nome_e_atrib_de_classe(cls):
        '''Retornando a classe  e os atributos'''
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
        p = Pessoa()
        print(p.cumprimentar())
        # acessando o atributo nome
        p.nome = 'Sombra'
        print(p.nome)
        g = Pessoa('Freitas', 40)
        print(g.nome)
        print(g.idade)
        ''' Trabalhanddo com atributos complexos '''
        cadu = Pessoa(nome='Carlos', idade=5)
        raildo = Pessoa(nome='Raildo')
        sombra = Pessoa(cadu, raildo, nome='Sombra', idade=40) #recebendo objetos...
        print(sombra.nome)
for filho in sombra.filhos:
    print(filho.nome)
    # python permite criar atributos em tempo de execução, exemplo !!!! não é boa prática!!!
    cadu.sobrenome = 'Freitas'
    print(cadu.sobrenome)
    # método __dict__ serve para verificar os atributos de um objeto
    print(cadu.__dict__)
    # del para remover um atributo
    # del cadu.sobrenome
    # Objeto cadu acessando o atributo de classe.
    print(cadu.olhos)
    # Acesso ao meétodo via classe e objeto:
    print(Pessoa.nome_e_atrib_de_classe(), cadu.nome_e_atrib_de_classe())
