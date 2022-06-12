"""
Created on Mon April 04 2022
@author: Silvana R Nobre
"""

import json


class iGenParams(object):
    DBFile = 'xx'
    DBType = 'sqlite3'
    DBAArea = 1
    DBVarToShow = 'Stand'
    DBToShow = 1

    def __init__(self, JasonFileName):
        with open(JasonFileName, "r") as f:
            jsonContent = f.read()
        RomeroInicialization = json.loads(jsonContent)
        iGenParams.DBFile = RomeroInicialization['DBFile']
        iGenParams.DBType = RomeroInicialization['DBType']
        iGenParams.DBAArea = int(RomeroInicialization['DBAArea'])
        iGenParams.DBVarToShow = RomeroInicialization['DBVarToShow']
        iGenParams.DBToShow = int(RomeroInicialization['DBToShow'])

    @classmethod
    def Update(cls, JasonFileName):
        x = {"DBFile": cls.DBFile,
             "DBType": cls.DBType,
             "DBAArea": str(cls.DBAArea),
             "DBVarToShow": cls.DBVarToShow,
             "DBToShow": str(cls.DBToShow)}
        with open(JasonFileName, "w") as f:
            f.write(json.dumps(x, indent=4))
