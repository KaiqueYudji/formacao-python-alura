from models.menu.item_menu import ItemMenu

class Drinking(ItemMenu):

    def __init__(self, name, price, size):
        super().__init__(name,price)#Isso quer dizer que eu estou enviando estes valores para o constructor da classe pai. Pois a classe pai já tem esse padrão definido
        self._size = size


    def __str__(self):
        return self._name


    def apply_discount(self):
        return super().apply_discount()

