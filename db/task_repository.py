from db.database import get_connection

# 1. code dublication, recommended to move helper function or context manager
# 2. no error handling
# 3. cursor not used as a context manager
# 4. no input validation

def add_task(title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()  # manual clean up better to use context managers


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks") # recommended to use SELECT id, title, completed FROM tasks
    tasks = cursor.fetchall()

    conn.close()
    return tasks


def mark_task_done(task_id): # suggestion: update_task_completed
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
