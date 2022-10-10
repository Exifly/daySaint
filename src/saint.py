
class Saint():
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "description": self.description
        }