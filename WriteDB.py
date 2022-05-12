"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""

from ReadDB import GlobalVar


# delete all the nodes that were created by InferenceEngine
def DeleteNodes(conn):
    SqlString = "Delete from Nodes where PreviousNode <> 0"
    cDelete = conn.cursor()
    cDelete.execute(SqlString)
    conn.commit()


# insert all the nodes that were created by InferenceEngine
def InsertNewNodes(conn):
    DeleteNodes(conn)
    FieldCount = len(GlobalVar.NodeClassAttrNameList)
    FilteredNodes = {key: value for (key, value) in GlobalVar.NodeDic.items() if value.PreviousNode != 0}
    NewNodesList = []
    for k in FilteredNodes.keys():
        NodeAttr = FilteredNodes[k]
        FieldList = '(NodeId '
        ExecStr = "NewNodesList.append((k "
        for field in GlobalVar.NodeClassAttrNameList:
            ExecStr += " , NodeAttr." + field
            FieldList += ", " + field
        FieldList += ') '
        ExecStr += "))"
        exec(ExecStr)
    RepeatMark = "?," * FieldCount
    SqlString = "INSERT into Nodes " + FieldList + "VALUES (" + RepeatMark + "?)"
    cInsert = conn.cursor()
    cInsert.executemany(SqlString, NewNodesList)
    conn.commit()
