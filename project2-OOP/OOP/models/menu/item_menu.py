from abc import ABC, abstractmethod

class ItemMenu(ABC):# Este abc está indicando que a classe ItemMenu é uma classe abstrata

    def __init__(self, name, price):
        self._name = name
        self._price = price


    @abstractmethod#Todas classes que herdarem da ItemMenu, deverão possuir este método. O polimorfismo poderá ser aplicado
    def apply_discount(self):
        self._price -= (self._price * 0.05)
