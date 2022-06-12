# https://towardsdatascience.com/python-interactive-network-visualization-using-networkx-plotly-and-dash-e44749161ed7
import dash
from dash import dcc
from dash import html
import DrawATree
import ReadDB
from iGenParams import iGenParams

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'iGen Viewer'

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

iGenParams('RomeroInitData.json')

conn = ReadDB.CreateConnection(iGenParams.DBFile)
ReadDB.GetDataToDraw(conn, iGenParams.DBAArea)

app.layout = html.Div([
    html.Div([html.H1("iGen Display Graph")],
             className="row",
             style={'textAlign': "center"}),
    html.Div([
        html.Div(
            className="eight columns",
            children=[dcc.Graph(id="my-graph",
                                figure=DrawATree.DrawATree(iGenParams.DBVarToShow,
                                                           iGenParams.DBToShow, True))]
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
