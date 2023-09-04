from typing import Literal


class __Prompt:
    ROLES = ("user", "assistant", "system")
    def __init__(self, role, content):
        assert role in self.ROLES, "Invalid role."
        self.__role = role
        self.__content = content
    
    @property
    def role(self): return self.__role

    @property
    def content(self): return self.__content

    @property
    def message(self) -> dict:
        return dict(role = self.role, content = self.content)

class Prompt(__Prompt):
    def __init__(
            self,
            role: Literal["user", "assistant", "system"],
            content: str):
        super().__init__(role, content)