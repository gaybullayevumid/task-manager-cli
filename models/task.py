class Task:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        if self.completed:
            status = "✅"
        else:
            status = "❌"
        return f"{self.id}. {self.title} [{status}]"