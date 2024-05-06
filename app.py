import os

restaurants = [
    {'name': 'Seu zé', 'category': 'churrascaria', 'activated': False},
    {'name': 'Sukya', 'category': 'japones', 'activated': True },
    {'name': 'Pecorino', 'category': 'italiano', 'activated': False }
]


def exhibit_program():
    '''This function is responsible per show for the user the title of our program
    
       Output
       -This funtion exhibit a message for the user like output
    '''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

""")
    

def exhibit_options():
    '''This function is responsible per exhibt all funcionalities that the user can do
    
       Output
       -This function show a sequence of messages that represents the menu of the application like output
    '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')


def back_to_main_menu():
    '''This function is responsible per return the user to the main menu
    
       Output
       -This function forwatd the user for the main menu like output
    '''

    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def exhibit_subtitle(text):
    '''This function is responsible per exhibit the subtitle of each section
    
       Input
       - This function receives the text that will be exhibited in the program

       Output
       - This function exhibit the subtitle of the section like output
    '''

    os.system('cls')
    line = '*' * ( len(text) )

    print(line)
    print(text)
    print(line)

    print()


def change_restaurant_status():
    '''This function is responsible per set the status of the restaurant selected by the user
    
       Output
       - This function changes the status of a restaurant and return the user to the main menu like output
    '''

    exhibit_subtitle('Alterando o status do restaurante')

    restaurant_name = input('Digite o nome do restaurante que você quer alterar: ')
    restaurant_exist = False

    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            restaurant_exist = True
            restaurant['activated'] = not restaurant['activated'] # Aqui o operador not é responsável por inverter valores
            message = f'O restaurante {restaurant_name} foi ativado com sucesso!' if restaurant['activated'] else f'O restaurante {restaurant_name} foi desativado com sucesso!'

            print(message)   

    if not restaurant_exist:
        print('O restaurante não foi encontrado')
    
    back_to_main_menu()


def invalid_option():
    '''This function is responsible per show for the user that the option selected by him is invalid and retuth him to the main menu
    
       Output
       - This function shows a message and return the user for the main menu like output
    '''

    print('Opção inválida!\n')
    back_to_main_menu()


def end_app():
    '''This function is responsible per exhibit a little text for showing to the user that the program is being closed
    
       Output
       - This function exhibts a message like output
    '''

    exhibit_subtitle('Encerrando app...')


def register_new_restaurant():
    '''This function is responsible per register a new restaurant
    
       Output
       - This function add a new restaurant to the list of restaurant like output
    '''
    
    exhibit_subtitle('Cadastro de novos restaurantes')

    restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurant_category = input('Digite a categoria do restaurante: ')
    restaurant_informations =  {'name': restaurant_name, 'category': restaurant_category, 'activated': False}
    
    restaurants.append(restaurant_informations)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso!\n')

    back_to_main_menu()


def list_restaurants():
    '''This function is responsible per list all restaurantes registred in the program
    
       Output
       - This function returns an array of restaurants like output 
    '''

    exhibit_subtitle('Listando os restaurantes')

    print( f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activated = 'Ativado' if restaurant['activated'] else 'Desativado'

        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_activated}')
    back_to_main_menu()
    

def choose_option():
    '''This function is responsible per to forward the user for the algorithm selected by the user
    
       Output
       - this function forward he user for the algorithm selected like output
    '''

    try:

        option_selected = int(input('Escolha uma opção: '))

        match option_selected:
            case 1:
                register_new_restaurant()
            case 2:
                list_restaurants()
            case 3:
                change_restaurant_status()
            case 4:
                end_app()
            case _:
                invalid_option()

    except Exception as error:
        print(error);invalid_option()



def main():
    '''This function is the main function, it is resopnsible per reload all algorithm
    
       Output
       - This function starts the program like output 
    '''

    os.system('dls')

    exhibit_program()
    exhibit_options()
    choose_option()


if __name__ == '__main__':
    main()
