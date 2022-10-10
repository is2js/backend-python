from functools import wraps
import jwt
from flask import request, jsonify
from .token_handler import token_creator


def token_verify(function: callable) -> callable:
    """Checking the valid Token and refreshing it. If not valid, return
    Info and stopping client request
    :parram - http request.headers: (Username / Token)
    :return - Json with the corresponding information.
    """

    @wraps(function)
    def decorated(*args, **kwargs):
        raw_token = request.headers.get("Authorization")
        uid = request.headers.get("uid")

        # if not raw_token:
        if not raw_token or not uid:
            return jsonify({"error": "Bad Request"}), 400

        try:
            token = raw_token.split()[1]
            # token_information = jwt.decode(token, key='1234', algorithms='HS256')
            token_information = token_creator.decode_token(token)
            token_uid = token_information["uid"]

        except jwt.InvalidSignatureError:
            return jsonify({"error": "Invalid Token"}), 498

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token is expired"}), 401

        except KeyError:
            return jsonify({"error": "Token is invalid"}), 401

        if int(token_uid) != int(uid):
            return jsonify({"error": "Unauthorized"}), 401

        next_token = token_creator.refresh(token)
        # route function
        # return function(*args, **kwargs)
        return function(next_token, *args, **kwargs)

    return decorated
