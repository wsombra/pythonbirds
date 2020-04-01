class Pessoa:
    # pra criar os atributos utilizo os método especial __init_(self)
                   # * QTD não definida |  parametros
     def __init__(self, *filhos,  nome=None, idade=40):
         # Atributos
         self.idade = idade
         self.nome  = nome
         # Atibuto filho recebe um list
         self.filhos = list(filhos)


     def cumprimentar(self):
        return f'Olá {id(self)}'

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