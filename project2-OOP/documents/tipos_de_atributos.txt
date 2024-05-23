
# Em Python, há uma distinção importante entre atributos de classe e atributos de instância:

## Atributos de Classe:
> São definidos diretamente na classe, fora de qualquer método.
> São compartilhados por todas as instâncias da classe.
> São acessados usando o nome da classe, seguido por um ponto e o nome do atributo (por exemplo, MinhaClasse.atributo).
> Podem ser utilizados para armazenar dados que são comuns a todas as instâncias da classe, como configurações padrão, constantes ou variáveis que devem ser compartilhadas entre todas as instâncias.

## Atributos de Instância:
> São definidos dentro de métodos da classe, geralmente dentro do método __init__, que é o construtor da classe.
> Pertencem a cada instância específica da classe.
> Cada instância tem sua própria cópia dos atributos de instância.
> São acessados usando self dentro dos métodos da classe (por exemplo, self.atributo).
> São usados para armazenar dados exclusivos de cada instância da classe, como propriedades específicas de um objeto.


## Os atributos de classe são acessados através do nome da classe. Por exemplo, se tivermos uma classe chamada MinhaClasse e um atributo de classe chamado atributo_de_classe, podemos acessá-lo diretamente usando MinhaClasse.atributo_de_classe.

## Por outro lado, os atributos de instância são acessados usando a palavra reservada self dentro dos métodos da classe. Por exemplo, se tivermos um atributo de instância chamado atributo_de_instancia, podemos acessá-lo dentro dos métodos da classe usando self.atributo_de_instancia.