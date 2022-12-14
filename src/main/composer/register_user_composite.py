from src.main.interface import RouteInterface
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository
from src.presenters.controllers import RegisterUserController


def register_user_composer() -> RouteInterface:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    user_repository = UserRepository()
    use_case = RegisterUser(user_repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
