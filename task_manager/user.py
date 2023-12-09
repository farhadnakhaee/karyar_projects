from project import Project
from task import Task


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.projects = []

    def create_project(self, project_id, title):
        project = Project(project_id, title)
        self.projects.append(project)
        return project

    def view_projects(self):
        return self.projects

    def __str__(self):
        return f"User: {self.username} - Projects: {len(self.projects)}"

if __name__ == "__main__":
    # Create Users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    # Create Projects
    project1 = user1.create_project(1, "Personal Tasks")
    project2 = user2.create_project(2, "Work Tasks")

    # Create Tasks
    task1 = Task(1, "Task 1", "Complete task 1", "2023-01-31")
    task2 = Task(2, "Task 2", "Finish task 2", "2023-02-15")

    # Add Tasks to Projects
    project1.add_task(task1)
    project2.add_task(task2)

    # Mark a Task as Completed
    task1.mark_as_completed()

    # View User's Projects
    print(user1)
    for project in user1.view_projects():
        print(f"  {project}")
        for task in project.tasks:
            print(f"    {task}")