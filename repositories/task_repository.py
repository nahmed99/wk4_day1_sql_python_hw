from db.run_sql import run_sql
from models.task import Task 

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s)"
    values = [task.description, task.assignee, task.duration, task.completed]
    run_sql(sql, values)


def select_all():  
    tasks = []  # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['description'], row['assignee'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks

