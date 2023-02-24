from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector("input[value='Add Project']").click()



    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath('//*[contains(@href,"edit_page.php?project_id=%s")]' % id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()




