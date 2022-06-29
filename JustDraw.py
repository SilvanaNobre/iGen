"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""
from support import DrawATree
from support import dbquery
import ReadDB
from iGenParams import iGenParams

if __name__ == '__main__':
    # read variables to Initialization
    iGenParams('RomeroInitData.json')
    dbquery.db = r'sqlite:///D:\Atrium\Projects\Silvana\_iGen\db\{0}'.format(iGenParams.DBFile)
    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    ReadDB.GetDataToDraw(iGenParams.DBAArea)

    DrawATree.DrawATreeMatplotlib(iGenParams.DBVarToShow, iGenParams.DBToShow)
# end JustDrow
