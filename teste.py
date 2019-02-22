class Pessoa:
    classe = 'mamifero'
    def __init__ (self, nome, cor_olhos):
        self.nome = nome
        self.cor_olhos = cor_olhos

    def cadastrar(self):
        print(f'{self.nome} Foi cadastrado no sistema')

    def excluir(self):
        print (f'{self.nome} Foi excluida')    

    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome
        print (f'{self.nome}  Você atualizou seus dados')


fulano = Pessoa('Suelen', 'castanho','preto','parda', 1.56)
cicrano = Pessoa('Creisson','verde','preto','preto', 1.40)


class Crianca(Pessoa):   #Herança, Criança herda tudo que a classe pessoa contém.
    def __init__ (self, desenho_favorito, brinquedos, nome, cor_olhos):
        self.desenho_favorito = desenho_favorito
        self.brinquedos = brinquedos
        Pessoa.__init__(nome, cor_olhos, cor_cabelo, cor_pele, altura) #

 henrique = Crianca('Boleto','azul','grisalho','vermelho', 0.50)           
print(henrique.nome)