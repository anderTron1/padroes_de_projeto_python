

from abc import ABCMeta, abstractmethod

# command 
class Ordem(metaclass=ABCMeta):
    @abstractmethod
    def executar(self):
        pass

# comandocoConcreto
class OrdemConcreta(Ordem):
    def __init__(self, acao):
        self.acao = acao
    
    def executar(self):
        self.acao.comprar()

class OrdemVenda(Ordem):
    def __init__(self, acao):
        self.acao = acao
    
    def executar(self):
        self.acao.vender()

class Acao:
    def comprar(self):
        print("Compra de ações")
    
    def vender(self):
        print("Venda de ações")
    
class Agente:
    def __init__(self):
        self.__fila_ordens = []
    
    def adicionar_ordem(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()
    
if __name__ == "__main__":
    acao = Acao()
    ordem_compra = OrdemConcreta(acao)
    ordem_venda = OrdemVenda(acao)
    agente = Agente()
    agente.adicionar_ordem(ordem_compra)
    agente.adicionar_ordem(ordem_venda)