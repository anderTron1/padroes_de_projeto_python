

from abc import ABCMeta, abstractmethod


# Interface
class Carteira(metaclass=ABCMeta):
    @abstractmethod
    def pagar(self):
        pass


# Objeto Real
class Banco(Carteira):
    def __init__(self):
        self.cartao = None
        self.conta = None

    def __get_conta(self):
        self.conta = self.cartao
        return self.conta
    
    def __tem_saldo(self):
        print(f"Banco :: Checando se a conta {self.conta} tem saldo")
        return True

    def set_cartao(self, cartao):
        self.cartao = cartao
    
    def pagar(self):
        if self.__tem_saldo():
            print(f"Banco :: Pagamento realizado com sucesso")
            return True
        else:
            print(f"Banco :: Falha no pagamento")
            return False

# Proxy
class CartaoDebido(Carteira):
    def __init__(self):
        self.banco = Banco()
    
    def pagar(self):
        cartao = input("Proxy:: Informe o número do cartão: ")
        self.banco.set_cartao(cartao)
        return self.banco.pagar()
    
# Cliente
class Cliente:
    def __init__(self):
        print("Cliente :: Quero comprar um refrigerente")
        self.cartao_debido = CartaoDebido()
        self.comprei = None
    
    def fazer_pagamento(self):
        self.comprei = self.cartao_debido.pagar()
    
    def __del__(self):
        if self.comprei:
            print("Cliente :: Compra realizada com sucesso")
        else:
            print("Cliente :: Compra não realizada")

if __name__ == '__main__':
    cl = Cliente()
    cl.fazer_pagamento()