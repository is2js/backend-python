from faker import Faker

from src.infra.test.user_repository_spy import UserRepositorySpy
from src.presenters.helpers.http_models import HttpRequest
from .find_user_controller import FindUserController
from src.data.test import FindUserSpy

faker = Faker()


def test_handle():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )

    response = find_user_controller.handle(http_request)

    print(response)

    # Testing Inputs
    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body is not None


def test_handler_no_query_param():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    print(response)

    # Testing Inputs
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}
    assert find_user_use_case.by_id_and_name_param == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body
