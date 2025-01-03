"""
INTRODUÇÃO AO PADRÃO DE PROJETO SINGLETON
Em resumo, quando usar:
1 - Garantir que um e somente um objeto de determinada classe seja instanciado;
2 - Oferecer um ponto de acesso para o objeto que seja global no programa;
3 - Controlar o acesso concorrente a recursos compartilhados;
"""

class Singleton(object):
    def __new__(cls):
        # hasattr verifica se o objeto tem o atributo passado neste caso o [instance]
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            #cls.nome = super(Singleton, cls).__new__(cls)
            print(f"Criando o objeto {cls.instance}")
        return cls.instance
    
s1 = Singleton()
print(f"Instância 1: {id(s1)}")
#s1.nome = "teste"
#print(s1.nome)
s2 = Singleton()
print(f"Instância 2: {id(s2)}")
#print(s2.nome)