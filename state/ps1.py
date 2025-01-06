"""

O padrão State é um dos padrões comportamentais do Design Patterns e é usado para permitir 
que um objeto altere seu comportamento quando seu estado interno muda. Ele é baseado na ideia de encapsular
 os estados possíveis de um objeto em classes separadas, promovendo a transição de estados de forma explícita e organizada.

Objetivo do Padrão State
    Organizar código complexo:
        Evitar grandes estruturas condicionais (como if-else ou switch) para gerenciar comportamentos baseados em estado.
    Facilitar manutenção:
        Tornar as regras de transição de estado mais claras e modulares.
    Promover extensibilidade:
        Permitir a adição de novos estados ou comportamentos sem modificar o código existente.

Componentes do Padrão State
    Contexto (Context):
        É o objeto que possui um estado interno.
        Mantém uma referência para o estado atual e delega a ele a execução de comportamentos.

    Estado (State):
        Define uma interface comum para todos os estados possíveis do objeto.

    Estados Concretos (Concrete States):
        Implementam o comportamento específico para um estado particular.
        Podem definir transições para outros estados.
"""

from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def manipular(self):
        pass

class StateConcretaA(State):
    def manipular(self):
        print("StateConcretaA")

class StateConcretaB(State):
    def manipular(self):
        print("StateConcretaB")

class Contexto(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def manipular(self):
        self.state.manipular()

if __name__ == '__main__':
    contexto = Contexto()
    stateA = StateConcretaA()
    stateB = StateConcretaB()

    contexto.set_state(stateA)
    contexto.manipular()

    contexto.set_state(stateB)
    contexto.manipular()