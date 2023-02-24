

def test_login(app):
    print (app.soap.get_projects_list("administrator", "root"))
