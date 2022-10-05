from typing import Dict, List
from src.domain.models import Pets, Users
from src.domain.test import mock_user
from src.domain.test import mock_pet


class RegisterPetSpy:
    """Class to define use case: Register Pet"""

    def __init__(self, pet_repository: any, find_user: any) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_param = {}

    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:

        self.register_param["name"] = name
        self.register_param["specie"] = specie
        self.register_param["user_information"] = user_information
        self.register_param["age"] = age

        response = None

        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": [mock_user()]}

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": [mock_user()]}

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = {"Success": True, "Data": [mock_user()]}

        else:
            return {"Success": False, "Data": None}

        return user_founded
