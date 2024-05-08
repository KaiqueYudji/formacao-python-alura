# Underscore before

Em Python, colocar um sublinhado antes do nome de uma variável é uma convenção para indicar que essa variável é privada. Isso significa que a variável não deve ser acessada ou modificada diretamente fora da classe ou do contexto em que foi definida. Por exemplo:

```
class MinhaClasse:
    def __init__(self):
        self._variavel_privada = 10

    def obter_variavel_privada(self):
        return self._variavel_privada

    def alterar_variavel_privada(self, novo_valor):
        self._variavel_privada = novo_valor

objeto = MinhaClasse()
print(objeto.obter_variavel_privada())  # Saída: 10
objeto.alterar_variavel_privada(20)
print(objeto.obter_variavel_privada())  # Saída: 20

```

Neste exemplo, _variavel_privada é uma variável privada da classe MinhaClasse, e é acessada e modificada apenas através de métodos da própria classe. O uso do sublinhado é uma convenção em Python para indicar que a variável é privada, mas na prática, ainda é possível acessá-la diretamente fora da classe. No entanto, é recomendado seguir essa convenção para facilitar a leitura do código e indicar a intenção de que a variável é privada.