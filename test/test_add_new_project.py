import random
import string

from model.project import Project


def test_add_new_project(app, db):
    old_list = app.soap.get_projects_list()
    project = Project(name=random_string("Project Name", 10))
    app.project.add_new(project)
    new_list = db.get_projects_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])