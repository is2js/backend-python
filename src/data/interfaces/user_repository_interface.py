from abc import ABC, abstractclassmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet repository"""

    @abstractclassmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractclassmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """abstractmethod"""

        raise Exception("Method not implemented")
