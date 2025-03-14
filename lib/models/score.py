from sqlalchemy import Column,Integer,ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Score(Base):
    __tablename__ = 'scores'
    __table_args__ = (UniqueConstraint(
        'student_id',
        'subject_id',
        name='_student_subject_uc'
        ),
    )
    id = Column(Integer, primary_key=True)
    _score = Column(Integer())
    student_id = Column(Integer(), ForeignKey('students.id'))
    subject_id = Column(Integer(),ForeignKey('subjects.id'))
    student = relationship('Student', back_populates='scores')
    subject = relationship('Subject',back_populates = 'scores')

    def __repr__(self):
        return f"Score {self.id}: {self.score}"
    
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if isinstance(score, int) and 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError("Score must be an integer between 0 and 100")
    @property
    def has_passed(self):
        return self._score >60 #assuming 60 is the passmark
    @property
    def summary(self):
        return f"Student {self.student.name}, Subject {self.subject.name}, Score: {self.score}"