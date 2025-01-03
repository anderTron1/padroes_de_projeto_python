
"""
O padrão Factory Simples é um padrão de design criacional que abstrai a lógica de criação de objetos, 
delegando-a para um método ou função específico. Em vez de criar objetos diretamente no código principal com new ou 
instanciando a classe, o padrão Factory fornece um ponto central para criar instâncias, o que melhora a flexibilidade 
e facilita a manutenção.

Características Principais
1 - Centralização da lógica de criação: Toda a lógica para instanciar objetos é encapsulada em um único local.
2 - Redução de dependências: O código principal não precisa conhecer os detalhes da criação de instâncias.
3 - Flexibilidade: Torna mais fácil adicionar novos tipos de objetos sem alterar o código cliente.

Estrutura do Padrão Factory Simples
    * Classe Factory:
        Responsável por encapsular a lógica de criação.
    * Produtos:
        Classes cujas instâncias serão criadas pela Factory.
    * Cliente:
         Código que utiliza a Factory para obter instâncias dos produtos.
"""

from abc import ABCMeta, abstractmethod 

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("O cachorro faz au au")

class Gato(Animal):
    def falar(self):
        print("O gato faz miau")


class Fabrica:
    def criar_animal(self, tipo):
        return eval(tipo)().falar()

if __name__ == "__main__":
    fab = Fabrica()
    animel = input("qual animal você quer ? [Cachorro, Gato]: ")
    fab.criar_animal(animel)