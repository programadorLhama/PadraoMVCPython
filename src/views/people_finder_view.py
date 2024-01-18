import os
from typing import Dict

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Determine o nome da pessoa para busca: ')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations

    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuario encontrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Name: { message["infos"]["name"] }
                Age: { message["infos"]["age"] }
                Height: { message["infos"]["height"] }
        '''
        print(success_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar usuario!

            Erro: { error }
        '''
        print(fail_message)