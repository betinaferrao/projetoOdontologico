class Consulta:
    def __init__(self, cliente, dentista):
        self.cliente = cliente
        self.dentista = dentista
        self.cod = None
        self.data = None
        self.preco = None
        self.hora_inicio = None

    def cadastrar_consulta(self):
        self.cod = str(input("Código: "))
        self.data = str(input("Data: "))
        self.preco = str(input("Preço da consulta: R$ "))
        livre = False
        while livre == False:
            self.hora_inicio = str(input("Hora início: "))
            livre = self.dentista.get_agenda().verificar_disponibilidade(self.hora_inicio)
        self.dentista.get_agenda().marcar_na_agenda(self.hora_inicio, self.cliente.get_nome())
        self.dentista.get_agenda().consultar_agendas()
        
    def mostrar_consultas(self):
        print("-" * 30)
        print("Paciente: {}".format(self.cliente.get_nome()))
        print("Horário: {}".format(self.hora_inicio))
        print("Dia: {}".format(self.data))
        print("Dentista: {}".format(self.dentista.get_nome()))
        print("Preço: R$ {}".format(self.preco))
        print("-" * 30)
       
    def excluir_consulta(self):
        self.dentista.get_agenda().marcar_na_agenda_livre(self.hora_inicio)

        print(self.dentista.get_agenda().consultar_agendas())
        print('-' * 30)
        print("Exclusão efetuada com sucesso!")
       

    def set_cliente(self, cliente):
        self.cliente = cliente
    def set_cod(self, cod):
        self.cod = cod
    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio
    def set_data(self, data):
        self.data = data
    def set_dentista(self, dentista):
        self.dentista = dentista
    def set_dentistas(self, dentistas):
        self.dentistas = dentistas
    def set_preco(self, preço):
        self.preço = preço
    
    def get_cliente(self):
        return self.cliente
    def get_cod(self):
        return self.cod
    def get_hora_inicio(self):
        return self.hora_inicio
    def get_data(self):
        return self.data
    def get_dentista(self):
        return self.dentista
    def get_dentistas(self):
        return self.dentistas
    def get_preco(self):
        return self.preço