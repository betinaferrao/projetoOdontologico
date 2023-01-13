from dentista import Dentista
from cliente import Cliente
from consulta import Consulta
from agenda import Agenda


# Lista de clientes
clientes = []
# Lista de consultas
consultas = []
# Lista de dentistas
dentistas = []

idC = 0
flag = False

# Cadastro de dentistas
print('=' * 30)
print("CADASTRO DE DENTISTAS")
print('=' * 30)
n = int(input("Deseja cadastrar quantos dentistas? "))
for i in range(n):
    print("-" * 20)
    print("CADASTRO DENTISTA {}".format(i+1))
    print("-" * 20)
    d = Dentista()
    d.cadastrar()
    dentistas.append(d)
    

S = 'S'
while S == 'S':
    print("-" * 40)
    print("Menu de clientes")
    print("-" * 40)
    print("Escolha uma operação: ")
    print("1- Cadastrar Cliente")
    print("2- Alterar informação de cliente")
    print("3- Consultar(nome, cpf ou ID)")
    print("4- Excluir cliente")
    print("5- Abrir menu de Consultas")
    print("6- Encerrar")
    op = int(input("Escolha uma operação: "))
    

    if op == 1: # Cadastro de cliente
        idC += 1
        print("Cadastro de cliente")
        c = Cliente(idC)
        c.cadastrar()
        clientes.append(c)
                

    elif op == 2: # Alterar informações do cliente
        print("Alterar informações do cliente")
        idCliente = int(input("Digite o ID do cliente: "))
        flag1 = False
                    
        for cli in clientes:
            if idCliente == cli.get_idC():
                cli.alterar_cliente()
                flag1 = True

        if flag1 == False:
            print("Id não cadastrado!")
                            
                
    elif op == 3: # Consultar cliente
        print("Consultar cliente")
        print("1- Consultar pelo ID")
        print("2- Consultar pelo nome")
        print("3- Consultar pelo CPF")
        consulta = int(input("Escolha a forma de consulta: "))

        if consulta == 1: # Consultar pelo ID
            c = int(input('Digite o ID: '))
            for cli in clientes:
                if c == cli.get_idC():
                    cli.consultar_pelo_idC()

        elif consulta == 2: # Consultar pelo Nome
            c = str(input('Digite o nome: '))
            for cli in clientes:
                if c == cli.get_nome():
                    cli.consultar_pelo_nome()

        else:  # Consultar pelo CPF
            c = str(input('Digite o CPF: '))
            for cli in clientes:
                if c == cli.get_cpf():
                    cli.consultar_pelo_cpf()

    elif op == 4: # Excluir cliente
        print('Excluir cliente')
        idC = int(input('Digite o ID do cliente: '))
                    
        for i, j in enumerate(clientes): # Percorre a lista de clientes
            if idC == j.get_idC():
                flag = j.excluir_cliente(clientes, i)
                break
            if flag == False:
                print("Id não cadastrado!")
            else:
                break
            
    elif op == 5: # Abre menu de consultas
        while S == 'S':
            print("-" * 30)
            print("Menu de consultas")
            print("-" * 30)
            print("Escolha uma operação: ")
            print("1- Cadastrar consulta (pelo CPF)")
            print("2- Ver todas consultas marcadas")
            print("3- Excluir consulta")
            print("4- Ver agenda de um dentista (por nome)")
            print("5- Ver agenda de todos dentistas")
            print("6- Retornar ao menu de clientes")
            print("7- Encerrar a execução")
            op = int(input("Escolha uma operação: "))
                    
            if op == 1: #Cadastro de consultas
                print("Cadastrar consulta (pelo CPF)")
                if(len(clientes)==0):
                    print('-' * 40)
                    print("Não há nenhum cliente adicionado! Primeiro realize o cadastro!")
                    break
                cpf_cliente = input("CPF do cliente: ")
                while not(len(cpf_cliente)==14):
                    print('Número inválido')
                    cpf_cliente = input("CPF do cliente: ")
                
                for i, dentista in enumerate(dentistas):
                    print(i+1, " - ",  dentista.get_nome())

                nome_dentista = input("Nome do dentista: ")
                for cliente in clientes:
                    if cpf_cliente == cliente.get_cpf():
                        cliente1 = cliente

                for dentista in dentistas:
                    if nome_dentista == dentista.get_nome():
                        dentista1 = dentista

                con = Consulta(cliente1, dentista1)
                con.cadastrar_consulta()
                consultas.append(con)
                flag = True
                
                if flag == False:
                    print('CPF não cadastrado!')
                    
                
            if op == 2: # Ver consultas marcadas
                print('=' * 30)
                print("Consultas marcadas")
                print('=' * 30)
                for consulta in consultas:
                    consulta.mostrar_consultas()
                if len(consultas) == 0:
                    print("Não há consultas marcadas! ")

            if op ==3: # Excluir consulta
                print('Excluir consulta')
                cod = str(input('Digite o código da consulta: '))
                    
                for i, consulta in enumerate(consultas): # percorre a lista de consultas
                    if cod == consulta.get_cod():
                        consulta.excluir_consulta()
                        consultas.remove(consulta)
                
            
            if op == 4: # Ver agenda de um dentista (por nome)
                for d in dentistas:
                    nome_dent = str(input("Nome do dentista: "))
                    if nome_dent == d.get_nome():
                        print(d.get_agenda().consultar_agendas())
                        break

            if op == 5: # Ver agenda de todos dentistas
                print('-' * 15)
                print("AGENDAS")
                print('-' * 15)
                for d in dentistas:
                    d.get_agenda().imprimindo_agendas()

            if op == 6: # Retorna ao menu de clientes
                break

            if op == 7: # Encerra o programa
                S = 'N'
            
    elif op == 6: # Encerra o programa
        break