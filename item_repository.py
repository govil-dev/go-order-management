# src/domain/repositories/item_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.models.item import Item

class ItemRepository(ABC):
    """Abstract base class for an item repository."""

    @abstractmethod
    def find_by_id(self, item_id: str) -> Optional[Item]:
        """Finds an item by its ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Item]:
        """Finds all items."""
        pass

    @abstractmethod
    def save(self, item: Item) -> None:
        """Saves an item."""
        pass

    @abstractmethod
    def delete(self, item_id: str) -> None:
        """Deletes an item by its ID."""
        pass
