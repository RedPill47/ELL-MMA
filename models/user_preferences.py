from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base

user_preferences = Table(
    'user_preferences',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('preference_id', Integer, ForeignKey('preferences.preference_id'), primary_key=True)
)