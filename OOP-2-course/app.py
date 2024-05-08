from models.restaurant import Restaurant

pecorino_restaurant = Restaurant('pecorino','italiano')
pecorino_restaurant.change_restaurant_status()

pecorino_restaurant.receive_rating('Kaique yudji', 5)
pecorino_restaurant.receive_rating('Bruna', 3)
pecorino_restaurant.receive_rating('Isa', 1)
pecorino_restaurant.receive_rating('Ubiracy', 1)
pecorino_restaurant.receive_rating('Sueli', 4)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()
