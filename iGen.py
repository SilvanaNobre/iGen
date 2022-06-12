"""
Created on Mon April 04 2022
@author: Silvana R Nobre
"""
import DrawATree
import ReadDB as db
import iGenParams
import WriteDB as wdb
from InferenceEngine import BuildATree
from iGenParams import iGenParams
from argparse import ArgumentParser


def ProcessCmdLine():
    parser = ArgumentParser(description='iGen, alternatives of forestry management generator.')
    parser.add_argument('-pp', '--projectpath', help='Path where project is stored or will be created',
                        type=str, required=True)
    parser.add_argument('-pt', '--projecttemplatepath', help='Project template to be cloned to project path',
                        type=str)
    return parser.parse_args()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read variables to Initialization
    args = ProcessCmdLine()
    print(args.projectpath)
    print(args.projecttemplatepath)
    iGenParams('RomeroInitData.json')

    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    conn = db.CreateConnection(iGenParams.DBFile)

    # Get all data needed from the database
    # InitVar.DBAArea also comes from initialization procedure
    db.GetData(conn, iGenParams.DBAArea)

    # create the Tree of alternatives from the Inference engine algorithm
    BuildATree()

    wdb.InsertNewNodes(conn)

    DrawATree.DrawATree(iGenParams.DBVarToShow, iGenParams.DBToShow)
    conn.close()
    # prepare other 2 databases with new rules and initial nodes
