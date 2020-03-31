class Pessoa:
    # pra criar os atributos utilizo os método especial __init_(self)
                      # parametro
     def __init__(self, nome=None, idade=40):
         # Atributo nome , passando um none type
         self.idade = idade
         self.nome  = nome


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

