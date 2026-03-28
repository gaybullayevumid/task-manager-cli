from db.task_repository import (
    add_task,
    get_all_tasks,
    mark_task_done,
    delete_task
)
from models.task import Task


# 1. no invalid input handling
#   - trimming
#   - empty values
#   - type checking
# 2. no error handling

def create_task(title):
    add_task(title)
    print("Task qo‘shildi!")


def list_tasks():
    tasks = get_all_tasks()

    if not tasks:
        print("Task yo‘q")
        return

    for t in tasks:
        task = Task(*t)
        print(task)


def complete_task(task_id):
    mark_task_done(task_id)
    print("Task bajarildi!")


def remove_task(task_id):
    delete_task(task_id)
    print("Task o‘chirildi!")
