"""
Created on Mon April 04 2022
@author: Silvana R Nobre
"""

import support.dbquery as dbquery

class BaseClass(object):
    def __init__(self, classtype):
        self._type = classtype


def ClassFactory(name, AttrList, BaseClass=BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # argnames variable is the one passed to the ClassFactory call
            if key not in AttrList:
                raise TypeError("Argument %s not valid for %s"
                                % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])

    newclass = type(name, (BaseClass,), {"__init__": __init__})
    return newclass


class RuleClass(object):
    def __init__(self, LastIntervention, NextIntervention):
        self.LastIntervention = LastIntervention
        self.NextIntervention = NextIntervention


class RuleConditionClass(object):
    def __init__(self, RuleId, IfOrThen, RuleVar, RuleExpression):
        self.RuleId = RuleId
        self.IfOrThen = IfOrThen
        self.RuleVar = RuleVar
        self.RuleExpression = RuleExpression


class TableSearchParamsClass(object):
    def __init__(self, Table, Key, Return):
        self.Table = Table
        self.Key = Key
        self.Return = Return


class GlobalVar(object):
    class NodeClass:
        pass

    # Horizon = 21
    # RegularNodeSize = 200
    # NoIntNodeSize = 50
    # ModelTitle = 'xx'
    FirstNode = 1
    LastNode = 99
    ParamDic = {}
    IntTDic = {}
    NodeDic = {}
    RuleDic = {}
    UpdateVarDic = {}
    NodeAttributeDic = {}
    SearchTableDic = {}
    RuleConditionList = []
    NodeClassAttrNameList = []
    NodeClassAttrStr = ' '


def GetSearchTableParams(FunctionStr) -> TableSearchParamsClass:
    tParams = TableSearchParamsClass(" ", " ", " ")
    fName = "SearchTable("
    lenfName = len(fName)
    lenFunction = len(FunctionStr)

    IniParams = FunctionStr.find(fName) + lenfName
    FindEndStr = FunctionStr
    Parentesis = 0
    EndParams = Parentesis
    while True:
        Parentesis = FindEndStr.find(')')
        FindEndStr = FindEndStr[(Parentesis + 1):]
        EndParams += Parentesis
        if len(FindEndStr) == 0:
            break

    Params = FunctionStr[IniParams:(EndParams + 1)].strip()
    IniTableParam = 0
    EndTableParam = Params.find(',')
    tParams.Table = Params[IniTableParam:EndTableParam]

    IniKeyParam = Params.find(',(') + 2
    EndKeyParam = Params.find('),')
    tParams.Key = Params[IniKeyParam:EndKeyParam].replace(':', '')

    IniReturnParam = EndKeyParam + 2
    EndReturnParam = lenFunction
    tParams.Return = Params[IniReturnParam:EndReturnParam]

    return tParams


# read the node variables with the update Rules
def GetVariables() -> dict:
    class ClassVar(object):
        def __init__(self, VarType, InitValue, UpdateRule):
            self.VarType = VarType
            self.InitValue = InitValue
            self.UpdateRule = UpdateRule

    def AjustTableSearch(uRule) -> str:
        if uRule.find("SearchTable") != -1:
            tSearchParams = GetSearchTableParams(uRule)
            NewTableParam = "'" + tSearchParams.Table + "'"
            NewReturnParam = "'" + tSearchParams.Return + "'"
            uRule = uRule.replace(tSearchParams.Table, NewTableParam)
            uRule = uRule.replace(tSearchParams.Return, NewReturnParam)
        return uRule

    SqlString = f"SELECT v.VariableId, v.VarType, v.NoIntNodeUpdateRule " + \
                "FROM Variable v " + \
                "WHERE v.Scope = 'Node'"
    variables = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for variable in variables:
        if variable[1][:3] == 'Int' or variable[1][:3] == 'int':
            iV = 0
        elif variable[1][:3] == 'Str' or variable[1][:3] == 'str':
            iV = 'x'
        elif variable[1][:3] == 'Dec' or variable[1][:3] == 'dec':
            iV = 0.1
        else:
            iV = '0'
        AjustedUpdateRule = AjustTableSearch(variable[2])
        LocalDic[variable[0]] = ClassVar(VarType=variable[1], InitValue=iV, UpdateRule=AjustedUpdateRule)
    return LocalDic


def GetClassAttrStr(VarDic) -> str:
    cAttr = "PreviousNode=-1, LiNode=-1"
    for k in VarDic.keys():
        cAttr = cAttr + ", " + k + "="
        if VarDic[k].VarType[:3] == 'Str' or VarDic[k].VarType[:3] == 'str':
            cAttr = cAttr + "'"
        cAttr = cAttr + str(VarDic[k].InitValue)
        if VarDic[k].VarType[:3] == 'Str' or VarDic[k].VarType[:3] == 'str':
            cAttr = cAttr + "'"
    return cAttr


def GetNameAttrList(VarDic) -> list:
    nList = []
    nList.append("PreviousNode")
    nList.append("LiNode")
    for k in VarDic.keys():
        nList.append(k)
    return nList


# read Nodes from the database
def GetInitialNodes(dbAnalysisArea) -> dict:
    FieldList = GlobalVar.NodeClassAttrNameList
    LastItem = len(FieldList)
    FieldStr = "n.NodeId"
    ClassStr = ""
    i = 1
    for f in FieldList:
        FieldStr = FieldStr + ", n." + f
        ClassStr += f + "=row[" + str(i) + "]"
        if i < LastItem:
            ClassStr += ","
        i += 1
    FieldStr = FieldStr + " "
    SqlString = f"SELECT {FieldStr} " +\
                "FROM Nodes as n INNER JOIN MgmUnit mu on mu.MgmUnitId = n.MgmUnit " +\
                f"WHERE n.NodeType = 'Initial' and mu.AArea = '{dbAnalysisArea}'"
    nodes = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for row in nodes:
        LocalDic[row[0]] = eval("GlobalVar.NodeClass(" + ClassStr + ")")
    return LocalDic


def GetAllNodes(dbAnalysisArea) -> dict:
    FieldList = GlobalVar.NodeClassAttrNameList
    LastItem = len(FieldList)
    FieldStr = "n.NodeId"
    ClassStr = ""
    i = 1
    for f in FieldList:
        FieldStr = FieldStr + ", n." + f
        ClassStr += f + "=row[" + str(i) + "]"
        if i < LastItem:
            ClassStr += ","
        i += 1
    SqlString = f"SELECT {FieldStr} " +\
                "FROM Nodes as n INNER JOIN MgmUnit mu on mu.MgmUnitId = n.MgmUnit " +\
                f"WHERE mu.AArea = '{dbAnalysisArea}'"
    nodes = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for row in nodes:
        LocalDic[row[0]] = eval("GlobalVar.NodeClass(" + ClassStr + ")")
    return LocalDic


# read the Intervention Types from the database
def GetInterventionTypes() -> dict:
    SqlString = "SELECT IntTypeId, NodeColor FROM InterventionType"
    InterventionTypes = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for InterventionType in InterventionTypes:
        LocalDic[InterventionType[0]] = InterventionType[1]
    return LocalDic


# read the rules from database
def GetRules(dbAnalysisArea) -> dict:
    SqlString = "SELECT r.RuleId, r.LastIntervention, r.NextIntervention " + \
                "FROM Rule r INNER JOIN ValidRule v on v.Rule = r.RuleId " + \
                f"WHERE v.AArea ='{dbAnalysisArea}'"
    rules = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for rule in rules:
        LocalDic[rule[0]] = RuleClass(rule[1], rule[2])
    return LocalDic


# read the rule conditions from database
def GetRuleConditions(dbAnalysisArea) -> list:
    SqlString = "SELECT r.RuleId, r.IfOrThen, r.RuleVar, r.RuleExpression " + \
                "FROM RuleCondition r INNER JOIN ValidRule v on v.Rule = r.RuleId " + \
                "WHERE v.AArea = '{dbAnalysisArea}'"
    RuleConditions = dbquery.executeSQL(SqlString)
    LocalList = []
    for RuleCondition in RuleConditions:
        LocalList.append(RuleConditionClass(RuleConditions[0], RuleCondition[1], RuleCondition[2], RuleCondition[3]))
    return LocalList


# read Yield Tables or similar tables from database
def GetSearchTable() -> dict:
    TableDic = {}
    TableValueDic = {}

    SqlTableString = "SELECT NoIntNodeUpdateRule FROM Variable " + \
                     f"WHERE NoIntNodeUpdateRule LIKE '%SearchTable(%' "
    tables = dbquery.executeSQL(SqlTableString)
    for table in tables:
        tSearchParams = GetSearchTableParams(table[0])
        SqlValueString = "SELECT " + tSearchParams.Key + " , " + tSearchParams.Return + " " + \
                         "FROM " + tSearchParams.Table
        values = dbquery.executeSQL(SqlValueString)
        ValueDic = {}
        for value in values:
            KeyLength = len(values) - 1
            ExprToEvaluate = "("
            for i in range(0, KeyLength):
                ExprToEvaluate = ExprToEvaluate + "rowv[" + str(i) + "]"
                if i < KeyLength - 1:
                    ExprToEvaluate = ExprToEvaluate + ","
            ExprToEvaluate = ExprToEvaluate + ")"
            KeyValue = eval(ExprToEvaluate)
            ValueIndex = KeyLength
            Value = value[ValueIndex]
            ValueDic[KeyValue] = Value
        TableValueDicKey = tSearchParams.Table + "_" + tSearchParams.Return
        TableValueDic[TableValueDicKey] = ValueDic
    return TableValueDic


# read General Parameters from the database
def GetGlobalVar(dbAnalysisArea) -> dict:
    SqlString = "SELECT Variable, ParameterValue " + \
                "FROM Parameter " + \
                f"WHERE AArea = '{dbAnalysisArea}'"
    parameters = dbquery.executeSQL(SqlString)
    LocalDic = {}
    for parameter in parameters:
        LocalDic[parameter[0]] = parameter[1]
    return LocalDic


# main function that gets all data needed in Inference Engine
def GetData(dbAnalysisArea):
    GlobalVar.UpdateVarDic = GetVariables()
    GlobalVar.NodeClassAttrNameList = GetNameAttrList(GlobalVar.UpdateVarDic)
    GlobalVar.NodeClass = ClassFactory("NodeClass", GlobalVar.NodeClassAttrNameList)

    # this Str will be used whenever we need to instantiate a NodeClass variable
    GlobalVar.NodeClassAttrStr = GetClassAttrStr(GlobalVar.UpdateVarDic)

    GlobalVar.NodeDic = GetInitialNodes(dbAnalysisArea)
    GlobalVar.IntTDic = GetInterventionTypes()
    GlobalVar.RuleDic = GetRules(dbAnalysisArea)
    GlobalVar.RuleConditionList = GetRuleConditions(dbAnalysisArea)
    GlobalVar.SearchTableDic = GetSearchTable()
    GlobalVar.ParamDic = GetGlobalVar(dbAnalysisArea)

    # FirstNode
    GlobalVar.FirstNode = min(GlobalVar.NodeDic.keys())
    # LastNode
    GlobalVar.LastNode = max(GlobalVar.NodeDic.keys())


# end of def GetData(Name,dbAnalysisArea):

# main function that gets all data needed just to draw a tree
def GetDataToDraw(dbAnalysisArea):
    GlobalVar.UpdateVarDic = GetVariables()
    GlobalVar.NodeClassAttrNameList = GetNameAttrList(GlobalVar.UpdateVarDic)
    GlobalVar.NodeClass = ClassFactory("NodeClass", GlobalVar.NodeClassAttrNameList)

    # this Str will be used whenever we need to instantiate a NodeClass variable
    GlobalVar.NodeClassAttrStr = GetClassAttrStr(GlobalVar.UpdateVarDic)

    GlobalVar.NodeDic = GetAllNodes(dbAnalysisArea)
    GlobalVar.IntTDic = GetInterventionTypes()
    GlobalVar.ParamDic = GetGlobalVar(dbAnalysisArea)

# end of def GetDataToDraw(Name,dbAnalysisArea):
