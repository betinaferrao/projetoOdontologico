from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, idC):
        Pessoa.__init__(self)
        self.idC = idC

    def cadastrar(self):
        super().cadastrar()
        
    def alterar_cliente(self):
        self.nome = str(input("Nome: "))
        cpf = str(input('Digite o CPF (xxx.xxx.xxx-xx): '))
        while not(len(cpf)==14):
            print('Valor inválido, digite sem espaços, utilizar ponto e espaço como no exemplo')
            cpf = str(input('Digite o seu cpf (xxx.xxx.xxx-xx): '))
        self.cpf = cpf
        sexo = str(input("Sexo (F/M): ")).upper()
        while not(sexo=='M' or sexo=='F'):
            print('Digito inválido!')
            sexo = str(input("Sexo (F/M): ")).upper()
        self.sexo = sexo
        telefone = str(input("Telefone (xx yxxxx-xxxx): "))
        while not(len(telefone)==13):
            print('Número inválido!')
            telefone = str(input("Telefone (xx yxxxx-xxxx): "))
        self.telefone = telefone
    
    def consultar_pelo_idC(self):
        print('-' * 30)
        print('ID:', self.get_idC())  
        print('Nome:', self.get_nome())
        print('CPF:', self.get_cpf())
        print('Sexo:', self.get_sexo())
        print('Telefone:', self.get_telefone())
        print('-' * 30)

    def consultar_pelo_nome(self):
        print('-' * 30)
        print('ID:', self.get_idC()) 
        print('Nome:', self.get_nome())
        print('CPF:', self.get_cpf())
        print('Sexo:', self.get_sexo())
        print("Telefone:", self.get_telefone())
        print('-' * 30)

    def consultar_pelo_cpf(self):
        print('-' * 30)
        print('ID:', self.get_idC()) 
        print('Nome:', self.get_nome())
        print('CPF:', self.get_cpf())
        print('Sexo:', self.get_sexo())
        print("Telefone:", self.get_telefone())
        print('-' * 30)
    
    def excluir_cliente(self, clientes, i):
        clientes.pop(i)
        print("Exclusão efetuada com sucesso!")
        flag=True
        return flag

    def set_idC(self, idC):
        self.idC = idC
    def get_idC(self):
        return self.idC