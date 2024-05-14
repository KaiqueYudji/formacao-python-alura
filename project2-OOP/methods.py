#print("Camiseta Unissex","Tamanho: P, M, G, GG","Material: 100% algodão","Cores disponíveis: Preto, Branco, Vermelho", sep ='\n')


""" sum_odd_numbers = 0

for i in range(1,11):

    if i % 2 != 0:
        print(i)
        sum_odd_numbers += i
 """



# -----------------------------------------------------------------------------



""" for i in range(0,10):
    print(10 - i) """



# -----------------------------------------------------------------------------



""" number_selected = int(input('Digite o número que deseja ver a tabuada: '))

for i in range (1,11):
    print(f'{number_selected} X {i} = {number_selected * i}') """
   


# -----------------------------------------------------------------------------



""" person = { 'name':'Rodrigo', 'age': 19 }

print(person)
person.update({'age': 20}) # altera o valor do campo nome
person.update({'job': "programmer"}) # add o campo job com o valor programmer
print(person) """



# -----------------------------------------------------------------------------


""" dictionary = {# Esse dicionário possui 3 chaves: nome, age, job
    'nome':'Kaique Yudji',
    'age': 18,
    'job': 'Programmer'
}

key = input('Digite a chave aqui: ')

if key in dictionary:# Se a chave existe no dicionário
    print('Chave EXISTE no dicionário')
else:
    print('Chave NÃO EXISTE no dicionário')
 """


# -----------------------------------------------------------------------------


dictionary1 = {
    'A': 1,
    'B': 2,
    'C': 3
}

print(dictionary1.get('C'))# O método get retorna o valor do campo que possui q chave 'C'