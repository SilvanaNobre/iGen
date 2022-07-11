from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

class SqlAlchemy(object):
    Conn = None
    Base = None
    Session = None

    def __init__(self, uri: str, tableList: list):
        engine = create_engine(uri)
        # Access/modifiy database using ORM
        SqlAlchemy.Session = Session(engine)
        # Access/mofdify database using SQL
        SqlAlchemy.Conn = engine.connect()
        # Get metadata from database for use in ORM access
        metadata = MetaData()
        metadata.reflect(engine, only=tableList)
        SqlAlchemy.Base = automap_base(metadata=metadata)
        SqlAlchemy.Base.prepare()

    @classmethod
    def Select(self, sql):
        try:
            return SqlAlchemy.Conn.execute(sql).fetchall()
        except Exception as e:
            raise e

    @classmethod
    def getValueFromDb(self, sql):
        rows = self.Select(sql)
        for row in rows:
            return row[0]
        return None

    @classmethod
    def getDictResultset(self, sql):
        return {row[0]: row[1] for row in self.Select(sql)}

    @classmethod
    def getJSONResultset(self, sql):
        return self.Select(sql).first()[0]

    @classmethod
    def getDataframeResultSet(self, sql):
        return pd.read_sql(sql, self.Conn)

    @classmethod
    def RunSql(self, sql: str):
        self.Conn.execute(sql)

