import attr
from attr import validators

UserIdDS = int
UserNameDS = str

@attr.s(frozen=True, hash=True)
class UserDS:
    user_id: UserIdDS = attr.ib(validator=validators.instance_of(int))
    name: UserNameDS = attr.ib(validator=validators.instance_of(str))
    
    def __hash__(self) -> int:
        return hash((self.user_id, self.name, UserDS))