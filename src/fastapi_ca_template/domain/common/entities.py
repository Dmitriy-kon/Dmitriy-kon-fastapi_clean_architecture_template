from dataclasses import dataclass
from typing import Generic, TypeVar

from fastapi_ca_template.domain.common.value_objects import ValueObject

# Создаёт переменную типа EntityId, которая ограничена типом ValueObject. 
# Это означает, что EntityId может быть любым подклассом ValueObject.
EntityId = TypeVar("EntityId", bound=ValueObject)


@dataclass
class Entity(Generic[EntityId]):
    id: EntityId