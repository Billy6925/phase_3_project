from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from .base import Base

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer(),primary_key = True)
    _name = Column(String(), nullable = False)
    scores = relationship('Score',back_populates = 'subject')

    def __repr__(self):
        return f"Subject {self.id}: {self.name}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name) >0:
            self._name = name
        else:
            raise ValueError("The name must be a non-empty string")