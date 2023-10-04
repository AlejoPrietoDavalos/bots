import attr
from attr import validators, asdict

ROLES_ALLOWED = ("user", "assistant", "system")


@attr.s(frozen=True)
class MsgGPT:
    """ Un mensaje está caracterizado por un `role` y `content`."""
    role: str = attr.ib(validator=validators.in_(ROLES_ALLOWED))
    content: str = attr.ib(validator=validators.instance_of(str))

    @property
    def json(self) -> dict:
        return dict(role=self.role, content=self.content)

    def to_json(self) -> dict:
        return asdict(self)