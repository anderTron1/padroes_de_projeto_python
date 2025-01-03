
"""
O Singleton é útil em cenários onde é necessário garantir que haja apenas uma instância de uma classe, como:

Controle de acesso a recursos compartilhados, como arquivos ou conexões com banco de dados.
Gerenciamento de estados globais de uma aplicação.
Implementação de caches ou registradores de configuração.

Instância única: Apenas uma instância da classe é criada, independentemente de quantas vezes o acesso for solicitado.
Acesso global: A instância é acessível globalmente, permitindo que diferentes partes do programa compartilhem a mesma instância.
Controle de ciclo de vida: A própria classe controla a criação e o gerenciamento da instância.
"""

class Singleton:
    __instance = None 
    def __init__(self):
        if not Singleton.__instance:
            print("O método __init__ foi chamado")
        else:
            print(f"A instância já foi criada: {self.getInstance()}")
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
s1 = Singleton() # A classe é inicializada, mas o objeto não é criado
print(f"Objeto criado agora: {Singleton.getInstance()}")

s2 = Singleton() # Instância já criada 
