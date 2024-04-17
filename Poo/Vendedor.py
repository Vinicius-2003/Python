class Vendedor():
    def __init__(self, nome): # método construtor
        self.nome = nome #self se refere a classe, nesse caso o nome se refere ao Vendedor.
        self.vendas = 0
        self.nascimento = 2003
    
    def vendeu(self, vendas): #aqui é o parâmetro do método
        self.vendas = vendas

    def anos(self):
        print(f"Você têm {2024 - self.nascimento} anos!")

    def meta(self, meta):
        if self.vendas > meta : 
            print(f"{self.nome}, bateu meta")
        else:
            print("Meta não atingida")
