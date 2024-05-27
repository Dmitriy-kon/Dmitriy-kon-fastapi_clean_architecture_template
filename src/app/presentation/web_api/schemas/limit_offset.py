from typing import Annotated

from pydantic import BaseModel
from fastapi import Query


class SLimitOffset(BaseModel):
    limit: Annotated[int, Query(default=20, le=100)]
    offset: Annotated[int, Query(default=0, le=100)]