from task import Task


class Project:
    def __init__(self, project_id, title):
        self.project_id = project_id
        self.title = title
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def __str__(self):
        return f"{self.title} - Tasks: {len(self.tasks)}"

