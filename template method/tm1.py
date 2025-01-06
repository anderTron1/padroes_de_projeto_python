
"""
O padrão Template Method é um padrão comportamental que define o esqueleto de um algoritmo em uma superclasse, permitindo
que as subclasses implementem partes específicas do algoritmo sem alterar sua estrutura geral.

Objetivo do Template Method
    Evitar duplicação de código: A lógica geral do algoritmo é definida em um único local (superclasse).
    Permitir personalização: Subclasses podem redefinir partes específicas do algoritmo para ajustar o comportamento sem mudar sua estrutura básica.
    Controlar o fluxo: Garante que o algoritmo siga uma sequência definida, enquanto permite extensibilidade.

Componentes do Template Method
    Classe Abstrata (AbstractClass):
        Define o esqueleto do algoritmo.
        Inclui o método template que chama outros métodos, alguns dos quais podem ser implementados pelas subclasses.

    Método Template:
        Um método que define a sequência do algoritmo.
        Pode chamar métodos concretos (já implementados) ou métodos abstratos (para implementação pelas subclasses).

    Subclasses Concretas (ConcreteClass):
        Implementam os métodos abstratos definidos pela classe base.
        Personalizam partes específicas do algoritmo.
"""

from abc import ABCMeta, abstractmethod

class Compilador(metaclass=ABCMeta):
    @abstractmethod 
    def coletar_fonte(self):
        pass 

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()

class CompiladorIOS(Compilador):
    def coletar_fonte(self):
        print("Coletando código fonte Swift")
    def compilar_objeto(self):
        print("Compilando código Swift para bytecode LLVM")
    def executar(self):
        print("Executando bytecode no interpretador")

class CompiladorAndroid(Compilador):
    def coletar_fonte(self):
        print("Coletando código fonte Kotlin")
    def compilar_objeto(self):
        print("Compilando código Kotlin para bytecode JVM")
    def executar(self):
        print("Executando bytecode no interpretador")

if __name__ == "__main__":
    ios = CompiladorIOS()
    ios.compilar_e_executar()

    print()
    android = CompiladorAndroid()
    android.compilar_e_executar()