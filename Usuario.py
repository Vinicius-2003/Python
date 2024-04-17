class Usuario:
    cargo = "Gerente"
    idade = 21

    def __init__(self):
        self.idade = 10

    def mostrar(self):
        print(f"Seu cargo é {self.cargo} e sua idade é {self.idade}")

    @staticmethod
    def mudar_cargo():
        Usuario.cargo = "Marco Jesus"

    def print(self):
        print(self.cargo)

if __name__ == "__main__":
    eu_testando = Usuario() #Instância objeto
    Usuario.mudar_cargo() #Chama método que altera valor da variável, sem criar um objeto para fazer isso
    eu_testando.mostrar()
    eu_testando.print()

# Static method mexe na class sem precisar instanciar nenhum objeto para usar o método ! No exemplo acima o metodo mudar_cargo, altera o valor da variável cargo. Ao chamar a função, nenhum objeto foi instanciado mas mesmo assim consegui alterar o valor da variável.


