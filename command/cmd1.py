

class Instalador:
    def __init__(self, fonte, destino):
        self.opcoes = []
        self.destino = destino 
        self.fonte = fonte 
    
    def preferencias(self, escolhas):
        self.opcoes.append(escolhas)   
    
    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f"Copiando os binários {self.fonte} para {self.destino}")
            else:
                print("Operação finalizada!")
    
if __name__ == "__main__":
    instalador = Instalador("python3", "/usr/bin/python3")
    instalador.preferencias({"python": True})
    instalador.preferencias({"java": False})
    instalador.executar()