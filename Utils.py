from typing import Any


class AttrDict:
    def __init__(self, dict_: dict) -> None:
        self._dict = dict_

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, name):
            print('Property')
        else:
            self.__dict[name] = value
        

