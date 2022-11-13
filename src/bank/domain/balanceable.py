from typing import Protocol


class Balanceable(Protocol):
    def getBalance(self) -> float: pass
    def getCurrency(self) -> str: pass
