from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Subject, Student, Score
from models.base import Base
import random

engine = create_engine('sqlite:///scoresheet.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    #Add subjects
    subjects = []
    subject_names = ["Maths", "English", "Chemistry","Music", "History"]
    for subject_name in subject_names:
        new_subject = Subject(name=subject_name)
        session.add(new_subject)
        subjects.append(new_subject)
        session.commit()
    #Add students and scores
    student_names = ["Alice", "Bob","Charlie","Kylian","Jude","Gabriel","Jesus","Adam","Ruth","Rachel"]
    for student_name in student_names:
        new_student = Student(name=student_name)
        session.add(new_student)
        session.commit()
        for subject in subjects:
            score_value = random.randint(0,100)
            new_score = Score(student_id = new_student.id, subject_id =subject.id,score = score_value)
            session.add(new_score)
        session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    seed_data()
    print("Data seeded")


