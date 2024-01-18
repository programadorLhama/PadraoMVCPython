from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_informations)
            self.__create_person_entity_and_store(new_person_informations)
            response = self.__format_response(new_person_informations)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __validate_fields(self, new_person_informations: Dict) -> None:
        if not isinstance(new_person_informations["name"], str):
            raise Exception('Campo Nome Incorreto!')

        try: int(new_person_informations["age"])
        except: raise Exception('Campo Idade Incorreto!')

        try: int(new_person_informations["height"])
        except: raise Exception('Campo Altura Incorreto!')

    def __create_person_entity_and_store(self, new_person_informations: Dict) -> None:
        name = new_person_informations["name"]
        age = new_person_informations["age"]
        height = new_person_informations["height"]

        new_person = Person(name, age, height)
        person_repository.registry_person(new_person)

    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }
