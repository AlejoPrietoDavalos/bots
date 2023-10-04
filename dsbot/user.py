import attr
from attr import validators, asdict


from typing import NewType

UserIdDS = NewType("user_id_ds", int)
UserNameDS = NewType("user_name_ds", str)

@attr.s(frozen=True, hash=True)
class UserDS:
    user_id: UserIdDS = attr.ib(validator=validators.instance_of(int))
    name: UserNameDS = attr.ib(validator=validators.instance_of(str))
    
    def __hash__(self) -> int:
        return hash((self.user_id, self.name, UserDS))