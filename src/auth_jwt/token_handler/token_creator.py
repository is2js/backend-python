import time
import jwt
from datetime import datetime, timedelta


class TokenCreator:
    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min

    def create(self, uid: int):
        """Return JWT
        :param - uid: user identify
        :return - string with token
        """

        return self.__encode_token(uid)

    def decode_token(self, token: str):
        """Decode token
        :param - stirng with token
        :return - string with token_information
        """
        token_information = jwt.decode(token, key=self.__TOKEN_KEY, algorithms="HS256")

        return token_information

    def refresh(self, token: str):
        """Function to create initial token when logging
        :parram - string with token
        :return - string with token
        """
        token_information = self.decode_token(token)
        token_uid = token_information["uid"]
        exp_time = token_information["exp"]

        if (exp_time - time.time()) / 60 < self.__REFRESH_TIME_MIN:
            # #If token refreshed in more than 15 minutes, new refresh
            return self.__encode_token(token_uid)

        return token

    def __encode_token(self, uid: int):
        """Encode and creating an jwt with payload
        :param - uid: user identify
        :return - string with token
        """
        token = jwt.encode(
            {
                "exp": datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN),
                "uid": uid,
            },
            key=self.__TOKEN_KEY,
            algorithm="HS256",
        )

        return token
