class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} LIKES'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} LIKES'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temp. - {self._likes} LIKES'

vingadores = Filme('Vingadores - guerra infinita', 2018, '160 min')
atlanta = Serie('atlanta', 2018,'2 temporadas')
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

print("=========================================================")

netflix_lista = [vingadores, atlanta]

for programa in netflix_lista:
    ##detalhes = programa.duracao if hasattr(programa,'duracao') else programa.temporadas
    print(programa)



