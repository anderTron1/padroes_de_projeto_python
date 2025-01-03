
"""
As metaclasses em Python são um recurso poderoso que permite definir como as classes são criadas. No contexto do padrão Singleton, metaclasses 
podem ser usadas para garantir que apenas uma instância de uma classe seja criada. Isso é feito controlando a criação de objetos na própria metaclasse.

O Papel das Metaclasses no Singleton
Em Python, uma metaclasse é uma classe especial responsável por criar outras classes. O uso de metaclasses no Singleton se dá porque elas permitem 
interceptar o processo de criação de classes (e instâncias), implementando a lógica necessária para garantir a existência de uma única instância.


"""

class University(type):
    """"
    Ele permite definir o comportamento de um objeto quando ele é "chamado" usando parênteses, como se fosse uma função.
    Ou seja, quando a função Geek for instanciada, essa função __calll__ será chamada.
    """
    def __call__(self, *args, **kwds):
        print(f"====Estes são os argumentos: {args}")
        
        return super().__call__(*args, **kwds)

class Geek(metaclass=University):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

obj = Geek("Felicity", 30)
print(obj.nome)
print(obj.idade)    

obj2 = Geek("Maria", 20)
print(obj2.nome)
print(obj2.idade)    

# Segundo exemplo
class SingletonMeta(type):
    """Metaclasse para implementar o padrão Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Se a classe ainda não possui uma instância, cria uma nova
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Classe que usa a metaclasse SingletonMeta
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Testando o Singleton
s1 = Singleton("Primeira Instância")
s2 = Singleton("Segunda Instância")

print(s1 is s2)  # True: Ambas as variáveis referenciam a mesma instância
print(s1.value)  # "Primeira Instância"
print(s2.value)  # "Primeira Instância"
