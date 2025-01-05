

from abc import ABCMeta, abstractmethod

# Asunto/Tópico
class AgenciaNoticias:
    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None
    
    def inscrever(self, incritos):
        self.__inscritos.append(incritos)
    
    def desinscrever(self, inscritos=None):
        if inscritos is None:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscritos)
    
    def notificar_todos(self):
        for insc in self.__inscritos:
            insc.notificar()

    #@adicionar_noticia.setter
    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia
    
    @property
    def mostrar_noticia(self):
        return f"Urgente: {self.__ultima_noticia}"

    def inscritos(self):
        return [type(insc).__name__ for insc in self.__inscritos]
    
#Interface Observer 
class TipoInscricao(metaclass=ABCMeta):
    @abstractmethod
    def notificar(self):
        pass

# Observador A
class InscritosSMS(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia}")

# Observador B
class InscritosEMAIL(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia}")

# Observador C
class InscritosOutroMeio(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)
    
    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia}")

#CLIENTE
if __name__ == "__main__":
    agencia_noticia = AgenciaNoticias()
    InscritosSMS(agencia_noticia)
    InscritosEMAIL(agencia_noticia)
    InscritosOutroMeio(agencia_noticia)

    print(f"Inscritos: {agencia_noticia.inscritos()}")

    agencia_noticia.adicionar_noticia("Nova noticia")
    agencia_noticia.notificar_todos()

    print(f"Descadastrando: {type(agencia_noticia.desinscrever()).__name__}")
    print(f"Inscritos: {agencia_noticia.inscritos()}")

    agencia_noticia.adicionar_noticia("Design Patterns em python!")
    agencia_noticia.notificar_todos()
