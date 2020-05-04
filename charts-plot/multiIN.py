# hello from github
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from  dash.dependencies import Input,Output
import plotly.express as px

df = pd.read_csv('patients-maroc.csv')
columns = df.columns
app = dash.Dash()
app.layout = html.Div([
                        html.Div([
                            dcc.Dropdown(id='xaxis',
                                         options=[{'label':i,'value':i} for i in columns],
                                         value= columns[0])
                        ],style={'width':'48%','display':'inline-block'}),
                       html.Div([
                            dcc.Dropdown(id='yaxis',
                                         options=[{'label':i,'value':i} for i in columns],
                                         value= columns[0])
                        ],style={'width':'48%','display':'inline-block'}),
                      html.Div([dcc.RadioItems(id='plot_name',
                                      options=[{'label':'Scatter-plot','value':'Scatter-plot'},
                                              {'label':'Line-chart','value':'Line-chart'},
                                              {'label':'Bar-chart','value':'Bar-chart'}],
                                       value = 'Bar-chart' 
                                      )]),
                        dcc.Graph(id='chart')
            ],style={'padding':'10%'})

@app.callback(Output('chart','figure'),
             [Input('xaxis','value'),
             Input('yaxis','value'),
             Input('plot_name','value')
             ])
def update_graph(xaxis_nm, yaxis_nm,plot_name):


    if plot_name  == 'Scatter-plot':
      return {'data':[go.Scatter(x=df[xaxis_nm],
                                y=df[yaxis_nm],
                                mode='markers')
                     ],

              'layaout':go.Layout(title='SCatter plot',
                                 xaxis={'title':xaxis_nm},
                                 yaxis={'title':yaxis_nm})
             }
    elif plot_name == 'Bar-chart' :
      return {'data':[go.Bar(x=df[xaxis_nm],
                                y=df[yaxis_nm],
                                )
                     ],

              'layaout':go.Layout(title='bar plot',
                                 xaxis={'title':xaxis_nm},
                                 yaxis={'title':yaxis_nm})
             }
    elif plot_name == 'Line-chart':
       return {'data':[go.Scatter(x=df[xaxis_nm],
                                y=df[yaxis_nm],
                                mode='lines')
                     ],

              'layaout':go.Layout(title='SCatter plot',
                                 xaxis={'title':xaxis_nm},
                                 yaxis={'title':yaxis_nm})
             }
    

if __name__ == '__main__':
    app.run_server()
