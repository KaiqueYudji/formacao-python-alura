from models.restaurant import Restaurant
from models.menu.drinking import Drinking
from models.menu.meal import Meal

juice = Drinking('Orange juice', 10, 'grande')
juice.apply_discount()

bread = Meal('Italian bread', 10, 'The best italian bread!')
bread.apply_discount()

pecorino_restaurant = Restaurant('pecorino','italiano')
pecorino_restaurant.add_to_menu(juice)
pecorino_restaurant.add_to_menu(bread)



def main():
    pecorino_restaurant.exhibit_menu

if __name__ == '__main__':
    main()
