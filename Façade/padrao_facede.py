

class GerenciamentoEventos:
    def __init__(self):
        print("GerencimentoEventos :: Vou organizar com todo mundo!\n")
    
    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()

class SalaoFestas:
    def __init__(self):
        print("SalaoFestas :: Agendando o salão de festas")

    def _esta_disponivel(self):
        print("SalaoFestas :: Salão de festa está disponível?\n")
        return True
    
    def agendar(self):
        if self._esta_disponivel():
            print("SalaoFestas :: Agendando o salão de festas\n")
        else:
            print("SalaoFestas :: Desculpe, o salão de festas não está disponível\n")

class Florista:
    def __init__(self):
        print("Florista :: Arranjando flores")
    
    def arranjar_flores(self):
        print("Florista :: Arranjando flores\n")

class Restaurante:
    def __init__(self):
        print("Restaurante :: Preparando comida")
    
    def preparar(self):
        print("Restaurante :: Preparando comida\n")

class Banda:
    def __init__(self):
        print("Banda :: Montando palco")
    
    def montar_palco(self):
        print("Banda :: Montando palco\n")

class Cliente:
    def __init__(self):
        print("Cliente :: Vou organizar um evento!\n")
    
    def contrata_gerente_eventos(self):
        print("Cliente :: vou contratar uma empresa para gerenciar eventos\n")

        ge = GerenciamentoEventos()
        ge.organizar()
    
    # é chamado quando o cliente for deletado da memória 
    def __del__(self):
        print("Cliente :: O evento foi um sucesso!\n")

if __name__ == "__main__":
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
    del cliente