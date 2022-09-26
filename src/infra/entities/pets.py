import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """defining Anymals Types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pets: [name={self.name!r}, specie={self.specie!r}, user_id={self.user_id}]"
