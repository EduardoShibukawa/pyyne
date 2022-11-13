from typing import Protocol


class Balanceable(Protocol):
    def balance(self) -> float: pass
    def currency(self) -> str: pass
