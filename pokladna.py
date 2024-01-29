from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional

@dataclass
class Polozka:
    kod: str
    nazev: str
    cena: float
    mnozstvi: int = 1

@dataclass
class Uctenka:
    polozky: list[Polozka]
    suma: float

class Pokladna(ABC):

    @abstractmethod
    def pridat_polozku(self, kod: str, mnozstvi: int) -> Optional[Polozka]:
        """
        Pridava polozku do seznamu polozek.
        """
        ...

    @abstractmethod
    def vratit_mezisoucet(self) -> float:
        """
        Vraci mezisoucet.
        """
        ...

    @abstractmethod
    def uctenka(self) -> Uctenka:
        """
        Vraci uctenku (seznam polozek a suma celkem).
        """
        ...

    @abstractmethod
    def vratit(self, zaplaceno: int) -> int:
        """
        Vraci castku, ktera ma byt vracena zakaznikovi.
        """
        ...

