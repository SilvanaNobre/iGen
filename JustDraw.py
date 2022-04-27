"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""
import ReadDB as db
import ReadInit
from ReadDB import GlobalVar as gv
from ReadInit import InitVar as init
import DrawATree as df

if __name__ == '__main__':
    # read variables to Initialization
    ReadInit.GetInit('RomeroInitData.json')

    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    conn = db.CreateConnection(init.DBFile)
    db.GetDataToDraw(conn, init.DBAArea)

    df.DrawATree(init.DBVarToShow, init.DBToShow)
# end JustDrow
