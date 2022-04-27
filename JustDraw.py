"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""
import DrawATree as df
import ReadDB as db
import ReadInit
from ReadInit import InitVar

if __name__ == '__main__':
    # read variables to Initialization
    ReadInit.GetInit('RomeroInitData.json')

    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    conn = db.CreateConnection(InitVar.DBFile)
    db.GetDataToDraw(conn, InitVar.DBAArea)

    df.DrawATree(InitVar.DBVarToShow, InitVar.DBToShow)
# end JustDrow
