import random

from model.project import Project


def test_delete_project(app, db):
    if len(db.get_projects_list()) < 1:
        app.project.add_new(Project())
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    old_projects.remove(project)
    new_projects = db.get_projects_list()
    assert new_projects == old_projects
