class Usuario:
    cargo = "Gerente"
    idade = 21

    def __init__(self, cargo, idade):
        self.cargo = cargo
        self.idade = idade

    def mostrar(self,nome):
        print(f"Seu cargo é {nome} e sua idade é {self.idade}")

eu = Usuario("Vini",21)
eu.mostrar("perícles")