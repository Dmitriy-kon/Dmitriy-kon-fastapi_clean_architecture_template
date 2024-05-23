from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    """ Base class for ORM models """
    __abstract__ = True
    
class TimeMixin():
    __abstract__ = True
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', NOW())"),
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', NOW())"),
        onupdate=text("TIMEZONE('utc', NOW())"),
    )