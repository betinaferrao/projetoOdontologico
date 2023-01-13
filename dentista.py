from pessoa import Pessoa
from agenda import Agenda

class Dentista(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.crm = None
        self.agenda = Agenda()
        
    def cadastrar(self):
        self.crm =  str(input("Crm: "))
        super().cadastrar()
        self.agenda.criar_agenda(self.get_nome())
    

    def set_crm(self, crm):
        self.crm = crm
    def set_agenda(self, agenda):
        self.agenda = agenda
    def get_crm(self):
        return self.crm
    def get_agenda(self):
        return self.agenda
        
    