from sys import maxsize


def status_to_text(status):
    status_dict = {30: "release", 10: "development", 50: "stable", 70: "obsolete"}
    return status_dict[int(status)]


class Project:
    def __init__(self, name="DefaultName", status="development", inherit_global=True, view_status="public", description="",
                 id=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.view_status, self.description)

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

