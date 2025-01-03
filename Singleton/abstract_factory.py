

from abc import ABCMeta, abstractmethod

# AbastractFactory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def criar_pizza_veg(self):
        pass

    def criar_pizza(self):
        pass    


# ConcretoFactory
class PizzaBrasileira(PizzaFactory):
    def criar_pizza_veg(self):
        return PizzaMandioca()
    
    def criar_pizza(self):
        return PizzaCamarao()

# ConcretoFactory b
class PizzaItaliana(PizzaFactory):
    def criar_pizza_veg(self):
        return PizzaBrocoli()
    
    def criar_pizza(self):
        return PizzaBolonha()
    
# AbstractProductA

class PizzaVeg(metaclass=ABCMeta):
    @abstractmethod
    def preparar(self, PizzaVeg):
        pass

# AbstractProductB
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def servir(self, Pizza):
        pass

## produtoContrego
class PizzaMandioca(PizzaVeg):
    def preparar(self):
        print(f"Preparando Pizza de Mandioca {type(self).__name__}")    

# ProdutoConcreto
class PizzaCamarao(Pizza):
    def servir(self, PizzaVeg):
        print(f"Servindo Pizza de Camarao {type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}")

# produtoContrego
class PizzaBrocoli(PizzaVeg):
    def preparar(self):
        print(f"Preparando Pizza de Brocoli {type(self).__name__}")

# ProdutoConcreto
class PizzaBolonha(Pizza):
    def servir(self, PizzaVeg):
        print(f"Servindo Pizza de Bolonha {type(self).__name__} é servida com bolonha na {type(PizzaVeg).__name__}")

# Cliente 

class Pizzaria:
    def fazer_pizza(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg() 
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)   


pizzaria = Pizzaria()
pizzaria.fazer_pizza()