import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

engine = sa.create_engine('sqlite:////tmp/pokemons.db', echo=True)
Base = declarative_base()


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = sa.Column(sa.Integer, primary_key=True)
    pokemon_name = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer)
