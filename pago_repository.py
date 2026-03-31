from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.pago import Pago

class PagoRepository(ABC):
    """
    Interfaz abstracta para el repositorio de pagos.
    Define los métodos que cualquier implementación de repositorio de pagos debe tener.
    """

    @abstractmethod
    def guardar(self, pago: Pago) -> None:
        """
        Guarda o actualiza una entidad de pago en el repositorio.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_id(self, pago_id: str) -> Optional[Pago]:
        """
        Busca una entidad de pago por su ID.
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_por_orden_id(self, orden_id: str) -> Optional[Pago]:
        """
        Busca una entidad de pago por el ID de la orden asociada.
        """
        raise NotImplementedError
