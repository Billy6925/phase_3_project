import click
from helpers import (
    exit_program,
    add_student,
    add_subject,
    add_score,
    update_score,
    get_all_students,
    find_student_by_id,
    find_subject_by_id,
    calculate_average,
    delete_student,
    calculate_points,
    rank_students,
    get_student_scores
)

@click.group()
def cli():
    pass

@cli.command()
def menu():
    while True:
        click.echo("Menu:")
        click.echo("0. Exit the program")
        click.echo("1. Add student")
        click.echo("2. Add Subject")
        click.echo("3. Add score")
        click.echo("4. Update score")
        click.echo("5. Get all students")
        click.echo("6. Find student by id")
        click.echo("7. Find subject by id")
        click.echo("8. Calculate_average")
        click.echo("9. Delete student")
        click.echo("10. Calculate points")
        click.echo("11. Rank students")

        choice = click.prompt("Choose an option", type =int)

        if choice == 0:
            exit_program()
        elif choice == 1:
            name = click.prompt("Enter student name")
            add_student(name)
            click.echo(f"{name} added successfully")
        elif choice == 2:
            name = click.prompt("Enter subject name")
            add_subject(name)
            click.echo(f'{name} added successfully')
        elif choice == 3:
            student_id = click.prompt("Enter student id",type = int)
            subject_id = click.prompt("Enter subject id", type = int)
            score = click.prompt("Enter score", type = int)
            add_score(student_id,subject_id,score)
            click.echo(f'{score} added')
        elif choice == 4:
            student_id = click.prompt("Enter student id",type = int)
            subject_id = click.prompt("Enter subject id", type = int)
            new_score = click.prompt("Enter new score", type = int)
            update_score(student_id, subject_id,new_score)
            click.echo(f'{new_score} updated')
        elif choice == 5:
            students = get_all_students()
            for student in students:
                click.echo(f"Student: {student['name']}")
                for score in student['scores']:
                    click.echo(f"Subject: {score['subject']}, {score['score']}")
                click.echo("-" * 40)
        elif choice == 6:
            student_id = click.prompt("Enter student id", type = int)
            student =find_student_by_id(student_id)
            click.echo(f"Student: {student.name}")
        elif choice ==7:
            subject_id = click.prompt("Enter subject id", type =int)
            subject =find_subject_by_id(subject_id)
            click.echo(f"Subject: {subject.name}")
        elif choice ==8:
            student_id = click.prompt("Enter student id", type = int)
            average = calculate_average(student_id)
            click.echo(f"The average is: {average}")
        elif choice == 9:
            student_id = click.prompt("Enter student id", type = int)
            delete_student(student_id)
            click.echo(f"Student {student_id} deleted")
        elif choice == 10:
            student_id = click.prompt("Enter student id", type = int)
            scores = get_student_scores(student_id)
            if scores:
                total_points = sum(calculate_points(score) for score in scores)
                click.echo(f"Points: {total_points}")
            else:
                click.echo("No scores found for the given student ID")
        elif choice == 11:
            ranking = rank_students()
            for rank, student in enumerate(ranking, start=1):
                click.echo(f"{rank}. {student['name']} with {student['total_points']} points")
        else:
            click.echo("Invalid choice")

if __name__ == '__main__':
    cli()

