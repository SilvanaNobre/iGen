from sqlalchemy import create_engine
import pandas as pd
import support.app_object as app_object_support

db = None

def getEngine(uri: str):
    return create_engine(uri)


def connectDB():
    engine = getEngine(db)
    return engine.connect()


def executeSQL(sql):
    conn = connectDB()
    try:
        return conn.execute(sql).fetchall()
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
