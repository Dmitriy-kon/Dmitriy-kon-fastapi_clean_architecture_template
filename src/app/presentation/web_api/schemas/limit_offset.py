from typing import Annotated

from fastapi import Query
from pydantic import BaseModel


class SLimitOffset(BaseModel):
    limit: Annotated[int, Query(default=20, le=100)]
    offset: Annotated[int, Query(default=0, le=100)]
