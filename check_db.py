from fixture.db import DbFixture

db = DbFixture(host="localhost", name="bugtracker", user="root",
               password="")

print(db.get_projects_list()[1].inherit_global)