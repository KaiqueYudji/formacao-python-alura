from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
     Endpoint que exibe uma mensagem incrível do mundo da programação!
    
     '''
    return {'Hello':'World'}


@app.get('/api/restaurantes/')
def get_restaurants(restaurant: str = Query(None)):
    '''
    git status
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_datas = response.json()
        if restaurant is None: return { 'Dados': json_datas }

        restaurant_datas = []

        for item in json_datas:
            if item['Company'] == restaurant:
                restaurant_datas.append(
                    {
                        'item': item['Item'],
                        'price': item['price'],
                        'description': item['description']
                    }
                )

        return {'Restaurante':restaurant, 'cardápio': restaurant_datas}
    else:
        print(f'ERRO: {response.status_code}')