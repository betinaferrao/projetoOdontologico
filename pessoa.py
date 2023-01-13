class Pessoa:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.sexo = None
        self.telefone = None

    def cadastrar(self):
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
        
    def set_nome(self, nome):
        self.nome = nome
    def set_cpf(self, cpf):
        self.cpf = cpf
    def set_sexo(self, sexo):
        self.sexo = sexo
    def set_telefone(self, telefone):
        self.telefone = telefone
    def get_nome(self):
        return self.nome
    def get_cpf(self):
        return self.cpf
    def get_sexo(self):
        return self.sexo
    def get_telefone(self):
        return self.telefone

    def __str__(self):
        print('A pessoa: ' + self.nome + "\n De CPF: " + self.cpf + "\n De telefone: " +
              self.telefone + " está cadastrada no sistema!")