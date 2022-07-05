import drawNetworkxPlotly

def CreateGraphFig(TreeGraph, TG_PosDic, colorList, sizeList, TG_LabelDic):
    fig = drawNetworkxPlotly.draw(TreeGraph, TG_PosDic, node_color=colorList, node_size=sizeList, labels=TG_LabelDic,
                                  font_size=8,
                                  font_color="black")

    fig.update_layout(
        yaxis={'visible': False, 'showticklabels': False},
        showlegend=False
    )
    return fig