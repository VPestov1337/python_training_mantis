__author__ = "Vitaliy Pestov"


from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, base_url, username, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(1)
        self.project = ProjectHelper(self)
        self.session = SessionHelper(self)
        self.soap = SoapHelper(self, username, password, base_url=base_url)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

