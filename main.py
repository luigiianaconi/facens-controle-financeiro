from models.transaction import Transaction

class Initialize():
    def show_menu(self):
        print(50*'-')
        print('Bem vindo ao controle financeiro')
        print(50*'-')
        print('1 - Adicionar transação')
        print('2 - Visualizar transações')
        print('3 - Sair')

    def choose_options(self):
        option = input('\nEscolha uma opção: ')
        if option not in ['1','2','3']:
            print('\nOpção inválida!')

        return option

    def to_add(self):
        operation = input('\nInforme o tipo da operação: ')
        value = input('\n Informe o valor: ')
        description = input('\nInforme a descrição: ')

        t = Transaction(operation, value, description)
        t.save()

        del t #Esse del não é obrigatório

    def to_view(self):
        Transaction().view()

    def to_go_out(self):
        print('\n Obrigado e volte sempre!')

if __name__ == '__main__':
    init = Initialize()

    option = ''

    while option != '3':
        init.show_menu()
        
        option = init.choose_options()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_go_out()