from abc import ABC
from typing import Dict
from src.domain.models import Pets


class RegisterPet(ABC):
    """Interface to RegisterPet use case"""

    @classmethod
    def register(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """use case"""

        raise Exception("Should implement method: register")
