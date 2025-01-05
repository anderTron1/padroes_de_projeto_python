
"""
Padrão de projeto Observer ele define uma relação de dependência um-para-muitos entre objetos, 
de forma que, quando um objeto (o sujeito) muda de estado, todos os seus dependentes (observadores) 
são notificados automaticamente e atualizados.

Objetivo do Padrão Observer
Desacoplamento: Permite que objetos observadores reajam a mudanças no sujeito sem que ele precise saber detalhes sobre esses observadores.
Comunicação eficiente: Atualiza automaticamente todos os observadores quando há uma alteração no estado do sujeito.

Componentes do Padrão Observer
Sujeito (Subject):

É o objeto que mantém o estado principal.
Gerencia a lista de observadores registrados.
Notifica os observadores sobre mudanças no estado.
Observadores (Observers):

São objetos que "observam" o sujeito.
Eles implementam uma interface para serem notificados de mudanças no sujeito.
Notificação:

O processo pelo qual o sujeito comunica mudanças aos observadores.


"""

class Objeto:
    def __init__(self):
        self.__observadores = []

    def __repr__(self):
        return "::Objeto::"

    def registrar(self, observador):
        self.__observadores.append(observador)
    
    def notificar_todos(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)

class ObservadorA:
    def __init__(self, objeto):
        objeto.registrar(self)
    
    def notificar(self, objeto, *args):
        print(f"O  {type(self).__name__} recebeu uma {args[0]} de {objeto}")

class ObservadorB:
    def __init__(self, objeto):
        objeto.registrar(self)
    
    def notificar(self, objeto, *args):
        print(f"O  {type(self).__name__} recebeu uma {args[0]} de {objeto}")


obj = Objeto()
obs = ObservadorA(obj)
obsB = ObservadorB(obj)

obj.notificar_todos("mensagem")