import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

params = ['c1', 'c2', 'c3']

app.layout = html.Div([
    dash_table.DataTable(
        id='table-editing',
        columns=(
            [{'id': 'model', 'name': 'model'}] +
            [{'id': p, 'name': p} for p in params]
        ),
        data=[
            dict(Model=i, **{param: 0 for param in params})
            for i in range(1,5)
        ],
        editable=True
    ),
    dcc.Graph(id='table-editing-output')
])

@app.callback(
    Output('table-editing-output', 'figure'),
    [Input('table-editing', 'data'),
     Input('table-editing', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'parcoords',
            'dimensions': [{
                'label': col['name'],
                'values': df[col['id']]
            } for col in columns]
        }]
    }

if __name__ == '__main__':
    app.run_server(debug=True)