"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""

from ReadDB import GlobalVar
from support import dbquery

# delete all the nodes that were created by InferenceEngine
def DeleteNodes():
    dbquery.executeSQL("Delete from Nodes where PreviousNode <> 0")


# insert all the nodes that were created by InferenceEngine
def InsertNewNodes():
    DeleteNodes()
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
    dbquery.executeMany(SqlString, NewNodesList)
    pass
