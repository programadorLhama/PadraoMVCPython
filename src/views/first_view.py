def introduction_page():
    message = '''
        Sistema Cadastral

        * Cadastrar Pessoa - 1
        * Buscar Pessoa Por Nome - 2
        * Sair - 5
    '''

    print(message)
    command = input('Comando: ')

    return command
