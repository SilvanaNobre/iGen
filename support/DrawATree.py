import matplotlib.pyplot as plt
import networkx as nx
from ReadDB import GlobalVar as gv
from support import drawNetworkxPlotly


class ClassSpaceNode(object):
    def __init__(self, iRow=1.0, Row=1.0, fRow=1.0):
        self.iRow = iRow
        self.Row = Row
        self.fRow = fRow

def CreateTreeGraph(FilteredNodeDic: dict,
              TG_ColorDic: dict, TG_SizeDic: dict, TG_LabelDic: dict, TG_PosDic: dict):

    # create the Graph, nodes and edges
    TreeGraph = nx.MultiDiGraph()
    TreeGraph.add_nodes_from(FilteredNodeDic.keys())
    for k in [k for k in FilteredNodeDic.keys() if FilteredNodeDic[k].PreviousNode != 0]:
        TreeGraph.add_edge(FilteredNodeDic[k].PreviousNode, k)

    # add colors
    nx.set_node_attributes(TreeGraph, TG_ColorDic, 'color')

    # add sizes
    nx.set_node_attributes(TreeGraph, TG_SizeDic, 'size')

    # add labels
    nx.set_node_attributes(TreeGraph, TG_LabelDic, 'label')

    # add position
    nx.set_node_attributes(TreeGraph, TG_PosDic, 'pos')

    pos = nx.drawing.layout.spring_layout(TreeGraph)
    for node in TreeGraph.nodes:
        TreeGraph.nodes[node]['pos'] = list(pos[node])
    return TreeGraph

def GetATree(VarToShow: str, WhatToShow: int):
    # create the Graph, nodes and edges
    FilteredNodeDic = {}
    eValStr = "NodeAttr." + VarToShow + "==" + str(WhatToShow)
    for k in gv.NodeDic.keys():
        NodeAttr = gv.NodeDic[k]
        if eval(eValStr):
            FilteredNodeDic[k] = NodeAttr
            if NodeAttr.PreviousNode == 0:
                FirstNode = k
                FirstPeriod = NodeAttr.Period

    # to design the tree-graph, we made each column a period
    # we need to know how many nodes there are in each period
    # that will be the total number of rows we are going to have
    # this is how many rows we are going to have in the graph,
    # the last year in the horizon is supposed to have the greatest amount of nodes
    h = int(gv.ParamDic['Horizon'])
    NodesCountHorizon = len({k: v for (k, v) in FilteredNodeDic.items() if v.Period == h})
    RowsCount = 20 * NodesCountHorizon

    # now we can calculate the space between nodes in each period
    PeriodNodes = {}  # key is a node - all the nodes in a particular Period
    RowPosNode = {}  # key is a node - the row each node will be positioned in the graph
    # the first node will be positioned just in the middle of the graph
    RowPosNode[FirstNode] = ClassSpaceNode()
    RowPosNode[FirstNode].Row = RowsCount / 2.0
    RowPosNode[FirstNode].iRow = 1.0
    RowPosNode[FirstNode].fRow = RowsCount

    # go through periods until the end of the horizon to calculate the position of each node
    for iPer in range(FirstPeriod + 1, int(gv.ParamDic['Horizon']) + 1):
        # filter the nodes of the period iPer
        PeriodNodes = {k: v for (k, v) in FilteredNodeDic.items() if v.Period == iPer}
        PrevNodesList = []

        # get the previous nodes of each node of the period and make a list with them
        Pn = 0
        for k in PeriodNodes.keys():
            Pn = PeriodNodes[k].PreviousNode
            if Pn not in PrevNodesList:
                PrevNodesList.append(Pn)

        # go through this list (list of the previous nodes) to calculate teh space we have to position next nodes
        for Pn in PrevNodesList:
            PvPeriodNodes = {k: v for (k, v) in PeriodNodes.items() if v.PreviousNode == Pn}
            NodesCount = len(PvPeriodNodes)
            NextSpace = (RowPosNode[Pn].fRow - RowPosNode[Pn].iRow + 1.0) / (NodesCount)
            PniRow = RowPosNode[Pn].iRow
            OpenNodesCount = len(PvPeriodNodes.keys())

            # divide the space we have among the next node, calculate the position of each one.
            for k in [k for k in PvPeriodNodes.keys()]:
                if OpenNodesCount == 1:
                    RowPosNode[k] = ClassSpaceNode()
                    RowPosNode[k].iRow = RowPosNode[Pn].iRow
                    RowPosNode[k].Row = RowPosNode[Pn].Row
                    RowPosNode[k].fRow = RowPosNode[Pn].fRow
                    PniRow = RowPosNode[k].fRow
                else:
                    RowPosNode[k] = ClassSpaceNode()
                    RowPosNode[k].iRow = PniRow
                    RowPosNode[k].Row = PniRow + NextSpace / 2.0
                    RowPosNode[k].fRow = PniRow + NextSpace
                    PniRow = RowPosNode[k].fRow

    TG_ColorDic = {}
    TG_SizeDic = {}
    TG_LabelDic = {}
    TG_PosDic = {}
    for iNode in FilteredNodeDic.keys():
        TG_PosDic[iNode] = (FilteredNodeDic[iNode].Period, RowPosNode[iNode].Row)
        TG_ColorDic[iNode] = gv.IntTDic[FilteredNodeDic[iNode].Intervention][0]
        TG_LabelDic[iNode] = FilteredNodeDic[iNode].Intervention
        if FilteredNodeDic[iNode].Intervention == 'ni':
            TG_SizeDic[iNode] = int(gv.ParamDic['NoIntNodeSize'])
            TG_LabelDic[iNode] = ''
        else:
            TG_SizeDic[iNode] = int(gv.ParamDic['RegularNodeSize'])
            TG_LabelDic[iNode] = FilteredNodeDic[iNode].Intervention

    TreeGraph = CreateTreeGraph(FilteredNodeDic, TG_ColorDic, TG_SizeDic, TG_LabelDic, TG_PosDic)
    return TreeGraph, TG_ColorDic, TG_SizeDic, TG_LabelDic, TG_PosDic

def DrawATreeMatplotlib(VarToShow: str, WhatToShow: int):
    TreeGraph, TG_ColorDic, TG_SizeDic, TG_LabelDic, TG_PosDic = GetATree(VarToShow, WhatToShow)
    ax = plt.gca()
    # title = gv.ParamDic['ModelTitle'] + " - " + VarToShow + ": " + str(WhatToShow) Não está sendo usado
    ax.set_title(gv.ParamDic['ModelTitle'])
    # add colors
    nx.set_node_attributes(TreeGraph, TG_ColorDic, 'color')
    colorList = list(nx.get_node_attributes(TreeGraph, 'color').values())

    # add sizes
    nx.set_node_attributes(TreeGraph, TG_SizeDic, 'size')
    sizeList = list(nx.get_node_attributes(TreeGraph, 'size').values())

    # add labels
    nx.set_node_attributes(TreeGraph, TG_LabelDic, 'label')

    # add position
    nx.set_node_attributes(TreeGraph, TG_PosDic, 'pos')
    nx.draw(TreeGraph, TG_PosDic, node_color=colorList, node_size=sizeList, font_size=8,
            font_color="black"
            , ax=ax
            )
    plt.axis('on')
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.get_yaxis().set_visible(False)
    plt.show()

def DrawATreePlotly(VarToShow: str, WhatToShow: int):
    TreeGraph, TG_ColorDic, TG_SizeDic, TG_LabelDic, TG_PosDic = GetATree(VarToShow, WhatToShow)
    colorList = list(nx.get_node_attributes(TreeGraph, 'color').values())
    sizeList = list(nx.get_node_attributes(TreeGraph, 'size').values())
    fig = drawNetworkxPlotly.draw(TreeGraph, TG_PosDic, node_color=colorList, node_size=sizeList, labels=TG_LabelDic,
                                  font_size=8,
                                  font_color="black")
    fig.update_layout(showlegend=False)
    return fig
