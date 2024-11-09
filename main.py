class Initialize():
    def __init__(self):
        self.__transactions = []

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

        self.__transactions.append(
            (operation, value, description)
        )

    def to_view(self):
        for transaction in __transactions:
            print(f'Operação: {transaction[0]} - Valor: {transaction[1]} - Descrição: {transaction[2]}')


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