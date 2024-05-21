# Crea el motor de SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

stage_str = "mssql+pyodbc://sa:112233445566@DESKTOP-73O4T2E/patitofeo?driver=ODBC+Driver+17+for+SQL+Server"


engine = create_engine(stage_str, pool_size=100, max_overflow=0)
Session = sessionmaker(bind=engine)


def consulta(query):
    session = Session()
    result = session.execute(text(query))
    rows = result.fetchall()
    session.close()
    return rows


def execute_sql(query):
    session = Session()
    result = session.execute(text(query))
    session.commit()
    session.close()
    return result
