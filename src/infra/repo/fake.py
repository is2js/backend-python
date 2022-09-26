# pylint: disable=E1101

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeRepo:
    """A simple Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str):
        """some thing"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
