class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome() : ")
        return self.__nome.title()
        # title retorna a primeira letra em maiuscula

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome() : ")
        self.__nome = nome
