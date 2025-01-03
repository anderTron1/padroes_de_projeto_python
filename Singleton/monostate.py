
"""
O padrão Monostate é uma variação do padrão Singleton. Enquanto o Singleton garante que apenas uma instância da classe exista, 
o Monostate permite que várias instâncias da classe sejam criadas, mas todas compartilhem o mesmo estado interno.

O padrão Monostate é útil quando você deseja simplificar a criação de objetos sem precisar controlar diretamente a quantidade de instâncias, 
mas ainda deseja que todas compartilhem um estado global
"""

class Monostate:
    __estado = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
        
m1 = Monostate()
print(f'm1 ID: {id(m1)}')
print(m1.__dict__)

m2 = Monostate()
print(f'm1 ID: {id(m2)}')
print(m2.__dict__)

m1.nome = "Felicity"
print(f"M1: {m1.__dict__}")
print(f"M2: {m2.__dict__}")