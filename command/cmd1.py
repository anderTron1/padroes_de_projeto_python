"""

O padrão de projeto Command é um dos padrões comportamentais do Design Patterns. Ele encapsula uma solicitação como um objeto,
 permitindo que você parametrize clientes com diferentes solicitações, faça o registro de solicitações ou suporte operações como desfazer e refazer ações.

Objetivo do Padrão Command
    Encapsulamento: Separar quem solicita a execução de uma ação (o cliente) de quem executa a ação (o receptor).
    Desfazer e Refazer: Facilitar a implementação de funcionalidades como "desfazer" e "refazer".
    Flexibilidade: Permitir o registro, armazenamento e execução de comandos dinamicamente.
    Extensibilidade: Adicionar novos comandos sem modificar o código existente.

Componentes do Padrão Command
    Command (Comando):
        Define a interface para todos os comandos.
    ConcreteCommand (Comando Concreto):
        Implementa o comando específico, chamando métodos no receptor.
    Receiver (Receptor):
        O objeto que realmente executa a ação.
    Invoker (Invocador):
        Solicita que o comando seja executado.
    Client (Cliente):
        Cria comandos concretos e os configura no invocador.

"""

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