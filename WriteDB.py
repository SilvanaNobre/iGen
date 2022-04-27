"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""

import sqlite3
from sqlite3 import Error
from ReadDB import GlobalVar as gv

# delete all the nodes that were created by InferenceEngine
def DeleteNodes(conn):
    SqlString = "Delete from Nodes where PreviousNode <> 0"
    cDelete = conn.cursor()
    cDelete.execute(SqlString)
    conn.commit()

# insert all the nodes that were created by InferenceEngine
def InsertNewNodes(conn):

    DeleteNodes(conn)
    FieldCount = len(gv.NodeClassAttrNameList)
    FilteredNodes = {key:value for (key,value) in gv.NodeDic.items() if value.PreviousNode != 0}
    NewNodesList = []
    for k in FilteredNodes.keys():
        NodeAttr = FilteredNodes[k]
        ExecStr = "NewNodesList.append((k "
        for field in gv.NodeClassAttrNameList:
            ExecStr += " , NodeAttr." + field
        ExecStr += "))"
        exec(ExecStr)
    RepeatMark = "?,"*FieldCount
    SqlString = "INSERT into Nodes VALUES (" + RepeatMark + "?)"
    cInsert = conn.cursor()
    cInsert.executemany(SqlString,NewNodesList)
    conn.commit()

