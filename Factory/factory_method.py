
"""
O padrão Factory Method é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, 
permitindo que as subclasses alterem o tipo de objetos que serão criados. Ele é usado para delegar a responsabilidade de 
instanciar objetos às subclasses, promovendo flexibilidade e reutilização de código.

Características do Padrão Factory Method
Encapsulamento da Criação:
    A lógica de criação dos objetos é centralizada, permitindo que o código que usa o objeto não precise se preocupar com detalhes de instância.
Personalização por Subclasses:
    Subclasses podem redefinir o método de fábrica para criar objetos específicos.
Redução de Acoplamento:
    O código cliente depende da interface ou classe abstrata, não da implementação concreta.

"""


from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):
    def __repr__(self):
        return "Seção Pessoal"

class secaoAlbum(Secao):
    def __repr__(self):
        return "Seção Album"
    
class SecaoProjeto(Secao):
    def __repr__(self):
        return "Seção Projeto"
    
class SecaoPublicacao(Secao):
    def __repr__(self):
        return "Seção Publicação"
    
class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.__secoes = []
        self.criar_perfil()
    
    @abstractmethod
    def criar_perfil(self):
        pass
    
    @property
    def secoes(self):
        return self.__secoes
    
    @secoes.setter
    def secoes(self, secao):
        self.__secoes.append(secao)

class Linkedin(Perfil):
    def criar_perfil(self):
        self.secoes = SecaoPessoal()
        self.secoes = secaoAlbum()
        self.secoes = SecaoProjeto()
        self.secoes = SecaoPublicacao()
    
class Facebook(Perfil):
    def criar_perfil(self):
        self.secoes = SecaoPessoal()
        self.secoes = secaoAlbum()

if __name__ == "__main__":
    rede_social = input("Qual rede quer criar o perfil [Linkedin, Facebook]: ")
    perfil = eval(rede_social)()
    print(f"Criando o perfil no(a) {type(perfil).__name__}")
    print(f"O perfil tem as seções: {perfil.secoes}")