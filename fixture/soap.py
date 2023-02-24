from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:
    def __init__(self, app, username, password):
        self.app = app
        self.client = client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        self.username = username
        self.password = password

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        projects_list = self.client.service.mc_projects_get_user_accessible(self.username, self.password)
        model_projects_list = []
        for project in projects_list:
            model_projects_list.append(Project(id=project.id, name=project.name, status=project.status.name,
                                               view_status=project.view_state.name, description=project.description))
        return model_projects_list
