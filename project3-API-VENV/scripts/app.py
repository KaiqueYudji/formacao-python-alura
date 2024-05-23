import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    json_datas = response.json()#Converte dados json em um dicionário python
    restaurant_datas = {}

    for item in json_datas:
        restaurant_name = item['Company']
        
        if restaurant_name not in restaurant_datas:
            restaurant_datas[restaurant_name] = []

        restaurant_datas[restaurant_name].append(
            {
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
            }
        )
else:
    print(f'O erro foi {response.status_code}')


# A primeira variável do for(teste) representa o primeiro campo retornado do: "restaurant_data.items()"
# A segunda variável representa o segundo cmpo retornado do: "restaurant_data.items()"

# retsaurant_name = chave | restaurant_data = valor da chave
for restaurant_name, restaurant_data in restaurant_datas.items():#items() retorna todos os pares de chave/valor contidos no dicionário
    file_name = f'{restaurant_name}.json'

    with open(file_name,'w') as file:# Este trecho de code é responsável por criar vários srquivos json
        json.dump(restaurant_data, file, indent=4)

