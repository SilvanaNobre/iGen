"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""
import DrawATree
import ReadDB
from iGenParams import iGenParams

if __name__ == '__main__':
    # read variables to Initialization
    iGenParams('RomeroInitData.json')

    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    conn = ReadDB.CreateConnection(iGenParams.DBFile)
    ReadDB.GetDataToDraw(conn, iGenParams.DBAArea)

    DrawATree.DrawATree(iGenParams.DBVarToShow, iGenParams.DBToShow,WebFigure=True)
# end JustDrow
