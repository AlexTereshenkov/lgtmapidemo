import yaml

class PasswordReader(object):

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as fh:
            return fh.readlines()

    def __repr__(self):
        return f"PasswordReader: {self.path}"


obj = yaml.load("""
!!python/object:__main__.PasswordReader
path: /etc/passwd
""")
print(obj)