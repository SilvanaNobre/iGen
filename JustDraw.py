"""
Created on Mon April 06 2022
@author: Silvana R Nobre

--db_root "s --sqlite:///db/{0}" --fname scatter.html --web
"""
from support import DrawATree
from support.dbquery import SqlAlchemy
import ReadDB
from iGenParams import iGenParams
import argparse

def ArgumentParse():
    parser = argparse.ArgumentParser(description='Draw an iGen diagram.')
    parser.add_argument('--web', action='store_true')
    parser.add_argument('--html_name', type=str)
    parser.add_argument('--db_root', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    parser = ArgumentParse()
    iGenParams('RomeroInitData.json')
    SqlAlchemy(parser.db_root.format(iGenParams.DBFile), ['Nodes'])
    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    ReadDB.GetDataToDraw(iGenParams.DBAArea)
    if parser.web:
        fig = DrawATree.DrawATreePlotly(iGenParams.DBVarToShow, iGenParams.DBToShow)
        fig.write_html(parser.html_name)
    else:
        DrawATree.DrawATreeMatplotlib(iGenParams.DBVarToShow, iGenParams.DBToShow)
# end JustDrow
