from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Subject, Score
from models.base import Base
import sys


engine = create_engine('sqlite:///scoresheet.db')
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Exiting the program.... Goodbye!")
    sys.exit()

def add_student(name):
    new_student = Student(name = name)
    session.add(new_student)
    session.commit()

def add_subject(name):
    new_subject = Subject(name = name)
    session.add(new_subject)
    session.commit()

def add_score(subject_id,student_id, score):
    new_score = Score(student_id = student_id, subject_id = subject_id,score = score)
    session.add(new_score)
    session.commit()

def update_score(student_id, subject_id, new_score):
    score = session.query(Score).filter_by(student_id= student_id, subject_id = subject_id).first()
    if score:
        score.score = new_score
        session.commit()
        return True
    return False

def get_all_students():
    result = []
    for student in session.query(Student).all():
        scores =[]
        for score in student.scores:
            subject = session.query(Subject).filter_by(id = score.subject_id).first()
            scores.append({'subject':subject.name, 'score':score.score})
        result.append({'name':student.name, 'scores': scores})
    return result

def find_student_by_id(student_id):
    return session.query(Student).filter_by(id = student_id).first()

def find_subject_by_id(subject_id):
    return session.query(Subject).filter_by(id = subject_id).first()

def calculate_average(student_id):
    scores = session.query(Score).filter_by(student_id = student_id).all()
    if scores:
        total = sum(score.score for score in scores)
        average = total/ len(scores)
        return average
    return None

def delete_student(student_id):
    student = session.query(Student).filter_by(id =student_id).first()
    if student:
        session.delete(student)
        session.commit()
        
def get_student_scores(student_id):
    student = find_student_by_id(student_id)
    if student:
        return [score.score for score in student.scores]
    else:
        return []

def calculate_points(score):
    if score >= 70 and score <=100:
        return 5 #grade A
    elif score >=60:
        return 4 #grade B
    elif score >= 50:
        return 3 #grade C
    elif score >= 40:
        return 2 #grade D
    else:
        return 1 # grade E
    
def rank_students():
    students = session.query(Student).all()
    ranking =[]
    for student in students:
        total_points = sum(calculate_points(score.score) for score in student.scores)
        ranking.append({'name': student.name, 'total_points': total_points})
    #sort students by total points in descending order
    ranking = sorted(ranking, key = lambda x: x['total_points'], reverse= True)
    return ranking
    



    