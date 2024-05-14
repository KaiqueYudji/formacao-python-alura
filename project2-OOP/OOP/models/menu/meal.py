from models.menu.item_menu import ItemMenu

class Meal(ItemMenu):#A classe meal está herdando os atributos e métodos da classe ItemMenu

    def __init__(self, name, price, description):
        #O super nos permite acessar informações de outras classes
        super().__init__(name, price)# A classe Meal está usando os atributos definidos através do constructor ItemMenu
        self._description = description


    def __str__(self):
        return self._name


    def apply_discount(self):
        self._price -= (self._price * 0.08)