from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.composer import register_user_composer, register_pet_composer

api_routes_bp = Blueprint("api_routes", __name__)


# @api_routes_bp.route("/api", methods=["GET"])
# @api_routes_bp.route("/api", methods=["POST"])
# def something():
# """test"""

# return jsonify({"message": request.args.to_dict()})
# return jsonify({"message": request.json})


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """register user route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }
        return jsonify({"data": message}), response.status_code

    # Handing Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pet():
    """register pet route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }
        return jsonify({"data": message}), response.status_code

    # Handing Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )
