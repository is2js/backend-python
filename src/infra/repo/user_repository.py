# pylint: disable=E1101
from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """insert data in user entity
        :param - name: person name
               - password: user password
        :return - tuple with new user inserted
        """

        InsertData = namedtuple("Users", "id name password")

        with DBConnectionHandler() as db_connection:
            try:
                new_uesr = Users(name=name, password=password)
                db_connection.session.add(new_uesr)
                db_connection.session.commit()

                return InsertData(
                    id=new_uesr.id, name=new_uesr.name, password=new_uesr.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
