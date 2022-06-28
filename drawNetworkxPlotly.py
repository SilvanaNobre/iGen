import plotly.graph_objects as go
import pandas as pd
import numpy as np

color_pattern = {'y': '#ffff00',
                 'b': '#0000ff',
                 'r': '#ff0000'}

gray_color = '#808080'

import networkx as nx

def draw(G, pos=None, ax=None, **kwds):
    if "with_labels" not in kwds:
        kwds["with_labels"] = "labels" in kwds

    fig = draw_networkx(G, pos=pos, ax=ax, **kwds)
    return fig


def draw_networkx(G, pos=None, **kwds):

    from inspect import signature

    valid_node_kwds = signature(draw_networkx_nodes).parameters.keys()
    valid_edge_kwds = signature(draw_networkx_edges).parameters.keys()

    node_kwds = {k: v for k, v in kwds.items() if k in valid_node_kwds}
    edge_kwds = {k: v for k, v in kwds.items() if k in valid_edge_kwds}

    if pos is None:
        pos = nx.drawing.spring_layout(G)

    fig = go.Figure()
    fig = draw_networkx_edges(G, pos, fig=fig, **edge_kwds)
    fig = draw_networkx_nodes(G, pos, fig=fig, **node_kwds)
    return fig

def draw_networkx_nodes(
    G,
    pos,
    fig,
    node_size,
    labels,
    nodelist=None,
    node_color="#1f78b4",
):

    if nodelist is None:
        nodelist = list(G)

    xy = np.asarray([pos[v] for v in nodelist])

    colors = [color_pattern[color] for color in node_color]

    customdata = list(labels.values())

    fig.add_scatter(x=xy[:, 0], y=xy[:, 1],
                    mode='markers',
                    customdata=customdata,
                    marker=dict(color=colors,
                                size=node_size,
                                opacity=1.0),
                    hovertemplate='%{customdata}'
                    )
    return fig


def draw_networkx_edges(
    G,
    pos,
    fig,
    edgelist=None
):
    if edgelist is None:
        edgelist = list(G.edges())

    edge_pos = np.asarray([(pos[e[0]], pos[e[1]]) for e in edgelist])

    line=dict(color=gray_color, width=1)
    for (src, dst) in edge_pos:
        x1, y1 = src
        x2, y2 = dst
        fig.add_scatter(x=[x1, x2], y=[y1, y2],
                        marker=dict(size=0),
                        line=line,
                        hovertext='',
                        hoverinfo='skip')
    return fig


