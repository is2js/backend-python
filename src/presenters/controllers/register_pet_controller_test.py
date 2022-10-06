from faker import Faker
from .register_pet_controller import RegisterPetController
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handle():
    """Testing Handle method"""

    register_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_controller = RegisterPetController(register_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    http_request = HttpRequest(body=attributes)
    response = register_pet_controller.route(http_request)

    print(response)

    # Testing inputs
    assert register_use_case.register_param["name"] == http_request.body["name"]
    assert register_use_case.register_param["specie"] == http_request.body["specie"]
    assert (
        register_use_case.register_param["user_information"]
        == http_request.body["user_information"]
    )
    assert register_use_case.register_param["age"] == http_request.body["age"]

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body
