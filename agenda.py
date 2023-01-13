class Agenda:
    def __init__(self):
        self.dono_agenda = None
        self.horario = {'8:00':'vago','8:30':'vago','9:00':'vago','9:30':'vago','10:00':'vago','10:30':'vago','11:00':'vago','11:30':'vago','13:00':'vago',
                    '13:30':'vago','14:00':'vago','14:30':'vago','15:00':'vago','15:30':'vago','16:00':'vago','16:30':'vago'}

    def criar_agenda(self, nome):
        self.dono_agenda = nome

    def imprimindo_agendas(self):    
        print(self.dono_agenda)
        for i, j in self.horario.items():
            print(i, ' - ', j)

    def verificar_disponibilidade(self, hora):
        if self.horario[hora] != 'vago':
            print('-' * 30)
            print("Horário ocupado! Marque outro horário!")
            livre = False
        else:
            print('-' * 30)
            print("Horário disponível!")
            livre = True
        return livre

    def marcar_na_agenda(self, hora, nome):   
        self.horario[hora] = ("Ocupado ({})".format(nome))

    def marcar_na_agenda_livre(self, hora):   
        self.horario[hora] = "vago"

    def consultar_agendas(self):
        for i, j in self.horario.items():
            print(i, ' - ', j)


    def set_dono_agenda(self, dono_agenda):
        self.dono_agenda = dono_agenda
    def get_dono_agenda(self):
        return self.dono_agenda
    def set_horario(self, horario):
        self.horario = horario
    def get_horario(self):
        return self.horario