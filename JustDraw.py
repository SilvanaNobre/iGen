"""
Created on Mon April 06 2022
@author: Silvana R Nobre
"""
from support import DrawATree
from support import dbquery
import ReadDB
from iGenParams import iGenParams
import argparse

def ArgumentParse():
    parser = argparse.ArgumentParser(description='Draw an iGen diagram.')
    parser.add_argument('--web', action=argparse.BooleanOptionalAction)
    parser.add_argument('--html_name', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    parser = ArgumentParse()
    iGenParams('RomeroInitData.json')
    dbquery.db = r'sqlite:///D:\Atrium\Projects\Silvana\iGen\db\{0}'.format(iGenParams.DBFile)
    # Init.DbFile comes from initialization variables read in ReadInit.GetInit
    # open the connection with the Database
    ReadDB.GetDataToDraw(iGenParams.DBAArea)
    if parser.web:
        fig = DrawATree.DrawATreePlotly(iGenParams.DBVarToShow, iGenParams.DBToShow)
        fig.write_html(parser.html_name)
    else:
        DrawATree.DrawATreeMatplotlib(iGenParams.DBVarToShow, iGenParams.DBToShow)
# end JustDrow
