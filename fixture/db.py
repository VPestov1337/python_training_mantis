import pymysql.cursors

from model.project import Project
from model.project import status_to_text


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_projects_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, enabled, view_state, description, inherit_global "
                           "from mantis_project_table")
            for row in cursor:
                (id, name, status, enabled, view_state, description, inherit_global) = row
                list.append(Project(id=id, name=name, description=description, inherit_global=int(inherit_global) > 0,
                                    view_status="public" if str(view_state) == "10" else "private",
                                    status=status_to_text(status)))
        finally:
            cursor.close()
        return list
