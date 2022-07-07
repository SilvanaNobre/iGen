from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pandas as pd
import support.app_object as app_object_support

db = None

engine = None

session = None

def getEngine(uri: str):
    return create_engine(uri)


def connectDB():
    global engine
    engine = getEngine(db)
    return engine.connect()


def executeSQL(sql):
    conn = connectDB()
    try:
        if 'SELECT ' in sql.upper():
            return conn.execute(sql).fetchall()
        else:
            with Session(engine) as session:
                engine.execute(sql)
                session.commit()
    except Exception as e:
        raise e


def getValueFromDb(sql):
    rows = executeSQL(sql)
    for row in rows:
        return row[0]
    return None

def getDictResultset(sql):
    return {row[0]: row[1] for row in executeSQL(sql)}


def getJSONResultset(sql):
    return executeSQL(sql).first()[0]


def getDataframeResultSet(sql):
    return pd.read_sql(sql, connectDB())

def executeMany(sql_mask: str, args_list: list):
    for args in args_list:
        sql = sql_mask
        for arg in args:
            sql = sql.replace('?', f"'{arg}'", 1)
        executeSQL(sql)
