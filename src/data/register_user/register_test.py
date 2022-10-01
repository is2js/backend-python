from faker import Faker
from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_register():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.name(),
    }

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing inputs
    assert user_repo.insert_user_param["name"] == attributes["name"]
    assert user_repo.insert_user_param["password"] == attributes["password"]

    # Tesing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method in fail"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        # "name": faker.name(),
        "name": faker.random_number(digits=2),
        "password": faker.name(),
    }

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing inputs
    assert user_repo.insert_user_param == {}

    # Tesing outputs
    assert response["Success"] is False
    assert response["Data"] is None
