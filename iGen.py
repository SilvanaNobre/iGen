"""
Created on Mon April 04 2022
@author: Silvana R Nobre
"""
import ReadDB as db
import WriteDB as wdb
import ReadInit
from ReadInit import InitVar as init
from InferenceEngine import BuildATree
import DrawATree as df

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read variables to Initialization
    ReadInit.GetInit('RomeroInitData.json')

    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    conn=db.CreateConnection(init.DBFile)

    # Get all data needed from the database
    # Init.DBAArea also comes from initialization procedure
    db.GetData(conn, init.DBAArea)

    # create the Tree of alternatives from the Inference engine algorithm
    BuildATree()

    wdb.InsertNewNodes(conn)

    df.DrawATree(init.DBVarToShow, init.DBToShow)
    conn.close()
    # prepare other 2 databases with new rules and initial nodes