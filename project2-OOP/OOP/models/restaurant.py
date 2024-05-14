# Métodos especiais dentro do python são formados por __método__. Os métodos __str__ e __init__ são métodos nativos de toda classe, mesmo que nós não criarmos, eles vão existir
# Os métodos especiais são conhecidos como "dunder methods"
from models.rating import Rating
from models.menu.item_menu import ItemMenu

class Restaurant:
    #Estes são atributos são atributos da classe
    #Para entender melhor a diferença entre atributos de classe e atributos de método leia o aruivo tipo_de_atributos.md
    restaurants = []

    def __init__(self, name, category): #"constructor" - self = this
        #Estes são atributos da instância
        #Para entender melhor a diferença entre atributos de classe e atributos de método leia o aruivo tipo_de_atributos.md
        self._name = name.title()# O método title sempre vai deixar a primrira letra do nome em maiúsculo
        self._category = category
        self._activated = False
        self._ratings = []
        self._menu = []

        self.restaurants.append(self)#Self representa a instância da classe que está sendo criada


    def __str__(self): # É um método especial responsável por exibir as informações da classe em string, com isso, apenas ao printar a instância da class, o que tem dentro do meu __str__ será exibido. Se o str for removido, ao printar apenas a instancia da class, será exibido apenas o endereço de memória da instância
        return f'{self._name} | {self._category}'

    
    @classmethod#Quando utilizamos este @, queremos dizer que este método pertence à classe em si, e não a uma instância da classe. Ou seja, não preciso instanciar a classe para acessar o método.
    def list_restaurants(cls):#O parâmetro é uma referência a própria classe(Restaurants), é usado para acessar atributos e métodos da classe(como se fosse o: Restaurant "a porópria classe")
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliação'.ljust(25)}')

        for restaurant in cls.restaurants:#O Restaurant.restaurants é utilizado pois o atributo "restaurants" é um atributo de classe
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.activated.ljust(24)} | {restaurant.rating_average}')


    @property
    def activated(self):
        return '✅' if self._activated else '❌' 


    def change_restaurant_status(self):#Método da instância, sem a instância não é possível acessar este método 
        self._activated = not self._activated


    def receive_rating(self, client, grade):
        if 0 < grade < 5:
            rating = Rating(client, grade)
            self._ratings.append(rating)
        else:
            print('Apenas valores entre 0 e 5 são aceitos')


    @property
    def rating_average(self):
        if not self._ratings:
            return '-'

        sum_of_ratings = sum(rating._grade for rating in self._ratings)
        total_qty_grade = len(self._ratings)
        average = round(sum_of_ratings / total_qty_grade, 1)

        return average


    def add_to_menu(self, item):
        if isinstance(item, ItemMenu):# Se o item que será inserido tiver a mesma estrutura de um item de cardápio
            self._menu.append(item)


    @property
    def exhibit_menu(self):
        print(f'Cardápio do restaurante {self._name}\n')

        for i, item in enumerate(self._menu, start=1):
            
            if hasattr(item, '_description'):
                print(f'{i}. Nome:{item._name.ljust(25)} | Preço: R${ str(item._price).ljust(25)} | Description: {item._description}')
            else:
                print(f'{i}. Nome:{item._name.ljust(25)} | Preço: R${ str(item._price).ljust(25)} | Size: {item._size}') 


#print(dir(pecorino_restaurant))#O dir é responsável por printar todos os atributos de um objeto(dicionário)
#print(vars(pecorino_restaurant))#O vars é responsável por exibir os atributos de um objeto(dicionário) no FORMATO de um dicionário


