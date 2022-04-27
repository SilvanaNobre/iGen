"""
Created on Mon April 04 2022
@author: Silvana R Nobre
"""

import json

class InitVar(object):
    DBFile = 'xx'
    DBType = 'sqlite3'
    DBAArea = 1
    DBVarToShow = 'Stand'
    DBToShow = 1

def GetInit(JasonFileName):

    jsonFile = open(JasonFileName, "r")
    jsonContent = jsonFile.read()
    RomeroInicialization = json.loads(jsonContent)

    InitVar.DBFile = RomeroInicialization['DBFile']
    InitVar.DBType = RomeroInicialization['DBType']
    InitVar.DBAArea = int(RomeroInicialization['DBAArea'])
    InitVar.DBVarToShow = RomeroInicialization['DBVarToShow']
    InitVar.DBToShow = int(RomeroInicialization['DBToShow'])

def SaveInit(JasonFileName):

    x = {"DBFile" : InitVar.DBFile,
         "DBType" : InitVar.DBType,
         "DBAArea" : str(InitVar.DBAArea),
         "DBVarToShow": InitVar.DBVarToShow,
         "DBToShow" : str(InitVar.DBToShow)}

    y = json.dumps(x, indent=4)

    jsonFile = open(JasonFileName, "w")
    jsonFile.write(y)
    jsonFile.close()




