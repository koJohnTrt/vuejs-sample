from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import *

from db import Base, engine


class RoadModel(Base):
    __tablename__ = "roads"
    create_date = Column("create_date", TIMESTAMP(timezone=False), nullable=False)
    create_code = Column("create_code", VARCHAR(20), nullable=False)
    create_pgm = Column("create_pgm", VARCHAR(20), nullable=False)
    update_date = Column("update_date", TIMESTAMP(timezone=False), nullable=False)
    update_code = Column("update_code", VARCHAR(20), nullable=False)
    update_pgm = Column("update_pgm", VARCHAR(20), nullable=False)
    rec_id = Column("rec_id", INTEGER, primary_key=True)
    code = Column("code", VARCHAR(4), nullable=False)
    name = Column("name", VARCHAR(20), nullable=False)
    date_from = Column("date_from", TIMESTAMP(timezone=False), nullable=False)
    date_to = Column("date_to", TIMESTAMP(timezone=False), nullable=False)

Base.metadata.create_all(bind=engine)
