from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL="mysql+pymysql://root:root@localhost/ticket_engine"


engine=create_engine(
    DATABASE_URL,
)

sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()



