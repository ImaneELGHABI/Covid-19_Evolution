# Necessary libraries
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

# Importing data
daily=pd.read_excel(r"daily.xlsx")
covid_map=pd.read_excel(r'map_data.xlsx')
covid_cases=covid_map[["Region",'Confirmed_cases']]
covid_cases.set_index('Region',inplace=True)
data_covid=pd.read_csv("https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/MA-times_series.csv")
region=pd.read_csv("https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv")
#Cleaning data
#The following line removes the first row because it contains undesirable values.
daily.drop(daily.index[0],inplace=True)
#The following command removes the columns whose names are declared.
daily.drop(columns=['New Cases 7-Day Moving Average','Cases Growth 7DMA','Total Deaths',
           'New Deaths 7DMA','Death Growth 7DMA','Adjusted CFR','Total Deaths per MM Population','Total Cases per MM Population',
       'Active Cases per ICU Bed'],inplace=True)
#Creation of the four variables needed later.
New_Cases=daily['New Cases'][1]
New_Recoveries=daily['New Recoveries'][1]
New_Deaths=daily['New Deaths'][1]
Actual_date=daily['Date'][1]
#Declare the "app" application that will contain our dashboard.
app=dash.Dash()
#Definition of the necessary HTML elements.
#The "layout" function gathers all the components used to design our dashboard.
#The "<Div>" tag groups the elements under block format.
app.layout=html.Div([html.Div(
# The "<H2>" tag is an HTML tag that signals second-level titles.
# "Children" presents the titles.
        html.H2(children='Dashbord Covid 19 Morocco',style={"text-align":"center"})),
                   html.Div(style={'width':'25%', 'backgroundColor':'rgb(242,242,242)', 'display':'inline-block', 'marginRight':'0%'},
                  children=[html.P(style={'textAlign':'center',
                                          'fontWeight':'bold','color':'purple','padding':'Irea'},
                                   children="Date"),
#The "<H3>" tag is an HTML tag that signals third-level titles.
                            html.H3(style={'textAlign':'center',
                                            'formatWeight':'bold', 'color':'purple'},
                                    children='{}'.format(Actual_date))]),

                     html.Div(style={'width':'25%', 'backgroundColor':'rgb(242,242,242)', 'display':'inline-block', 'marginRight':'0%'},
                  children=[html.P(style={'textAlign':'center',
                                          'fontWeight':'bold','color':'rgb(102, 102, 102)','padding':'Irea'},
                                   children="New cases"),
                            html.H3(style={'textAlign':'center',
                                            'formatWeight':'bold', 'color':'rgb(102, 102, 102)'},
                                    children='{}'.format(New_Cases))]),
        html.Div(style={'width':'25%', 'backgroundColor':'rgb(242,242,242)', 'display':'inline-block', 'marginRight':'0%'},
                  children=[html.P(style={'textAlign':'center',
                                          'fontWeight':'bold','color':'rgb(56, 166, 165)','padding':'Irea'},
                                   children="New recovered"),
                            html.H3(style={'textAlign':'center',
                                            'formatWeight':'bold', 'color':'rgb(56, 166, 165)'},
                                    children='{}'.format(New_Recoveries))]),
        html.Div(style={'width':'25%', 'backgroundColor':'rgb(242,242,242)', 'display':'inline-block', 'marginRight':'0%'},
                  children=[html.P(style={'textAlign':'center',
                                          'fontWeight':'bold','color':'rgb(204, 102, 119)','padding':'Irea'},
                                   children="New Deaths"),
                            html.H3(style={'textAlign':'center',
                                            'formatWeight':'bold', 'color':'rgb(204, 102, 119)'},
                                    children='{}'.format(New_Deaths))]),
#The dcc.Graph function corresponds to the generation of graphs and their insertion in the dashboard
                     html.Div(dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=data_covid['Dates/التواريخ'],
                y=data_covid['Cases/الحالات'],
                name='Confirmed cases',
                marker=dict(
                    color='rgb(102, 102, 102)'
                )
            ),
            dict(
                x=data_covid['Dates/التواريخ'],
                y=data_covid['Deaths/الوفيات'],
                name='Deaths',
                marker=dict(
                    color='rgb(204, 102, 119)'
                )
            ),
            dict(
                x=data_covid['Dates/التواريخ'],
                y=data_covid['Recovered/تعافى'],
                name='Recovered',
                marker=dict(
                    color='rgb(56, 166, 165)'
                )
            )
        ],
        layout=dict(
            title='Confirmed cases,deaths and recovered in Morocco',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=80)
        )
    ),
    style={'height': 300},
    id='my-graph3')),
               html.Div(dcc.Graph(figure=dict(
        data=[
            dict(
                x=daily['Date'],
                y=daily['Recovery Rate'],
                name='Recovery rate',
                marker=dict(
                    color='green'
                )
            )],layout=dict(
            title='Recovery Rate in Morocco',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=80)
        )
    ),
    style={'height': 300},
    id='my-graph1')),

                 html.Div(dcc.Graph(figure=dict(
        data=[
            dict(
                x=daily['Date'],
                y=daily['Case Fatality Rate (CFR)'],
                name='Case Fatality Rate',
                marker=dict(
                    color='red'
                )
            )],layout=dict(
            title='Mortality Rate in Morocco',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=80)
        )
    ),
    style={'height': 300},
    id='my-graph2')),

    html.Div(dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=daily['Date'],
                y=daily['New Cases'],
                name='New Confirmed cases',
                marker=dict(
                    color='rgb(102, 102, 102)'
                )
            ),
            dict(
                x=daily['Date'],
                y=daily['New Deaths'],
                name='New Deaths',
                marker=dict(
                    color='rgb(204, 102, 119)'
                )
            ),
            dict(
                x=daily['Date'],
                y=daily['New Recoveries'],
                name='New Recoveries',
                marker=dict(
                    color='rgb(56, 166, 165)'
                )
            )
        ],
        layout=dict(
            title='New Confirmed cases,deaths and recovered in Morocco',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=80)
        )
    ),
    style={'height': 300},
    id='my-graph')),
     html.Div(dcc.Graph(figure= px.pie(region, values='Total Cases / إجمالي الحالات', names='Region / الجهة', title="COVID-19 Cases distribution",color_discrete_sequence=px.colors.diverging.Tealrose_r))),

    html.Div(dcc.Graph(
     figure=go.Figure(
    data=[
        go.Bar(
            name="Recovered",
            x=region['Region / الجهة'],
            y=region['Total Recovered / إجمالي المعافين'],
           marker=dict(color='rgb(56, 166, 165)')        ),
        go.Bar(
            name="Deaths",
            x=region['Region / الجهة'],
            y=region['Total Deaths / إجمالي الوفيات'],
            marker=dict(color='rgb(204, 102, 119)')

        )
    ],
    layout=go.Layout(
        title="Deaths VS Recovered",
        yaxis_title="Total",

        ))
        )),
    html.Div(dcc.Graph(
        figure = px.bar(daily,x="Date",y="New Cases",orientation="v",
             height=600,title="Daily Confirmed cases",color="New Cases",color_continuous_scale=px.colors.diverging.Tealrose)

             )),

     html.Div(dcc.Graph(
        figure = px.bar(daily,x="Date",y="New Deaths",orientation="v", color="New Deaths",color_continuous_scale=px.colors.diverging.Tealrose,
             height=600,title="Daily New Deaths")

             )),
     html.Div(dcc.Graph(
        figure = px.bar(daily,x="Date",y="New Recoveries",color="New Recoveries",orientation="v",
             height=600,title="Daily New Recoveries",color_continuous_scale=px.colors.diverging.Tealrose)

             )),

    html.H1('COVID-19 Map'),
#We use the <Iframe> tag because we have to insert another html file which contains the map already prepared in our dashboard html file

    html.Iframe(id='map', srcDoc=open(r'map.html',"r", encoding="utf-8").read(), width='100%', height='600'),
#La balise <Boutton> aide à quitter l'application
    html.Button(id='map-submit-button', n_clicks=1, children='Submit'),

        html.H1('COVID-19_New Cases Distribution'),
    html.Iframe(id='map0', srcDoc=open(r'index.html',"r", encoding="utf-8").read(), width='100%', height='600'),
    html.Button(id='map-submit-button0', n_clicks=1, children='Submit'),

        html.H1('COVID-19_New Recoveries Distribution'),
    html.Iframe(id='map1', srcDoc=open(r'index1.html',"r", encoding="utf-8").read(), width='100%', height='600'),
    html.Button(id='map-submit-button1', n_clicks=1, children='Submit'),

        html.H1('COVID-19_New Deaths Distribution'),
    html.Iframe(id='map2', srcDoc=open(r'index2.html',"r", encoding="utf-8").read(), width='100%', height='600'),
    html.Button(id='map-submit-button2', n_clicks=1, children='Submit'),


    ])

#<@app.callback> the callback is used to be sure that a function will execute well after another. It is a synchronous callback, the code executing in one go and after.
@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button', 'n_clicks')])


def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open(r'map.html',"r", encoding="utf-8").read()

@app.callback(
    dash.dependencies.Output('map0', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button0', 'n_clicks')])


def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open(r'index.html',"r", encoding="utf-8").read()

@app.callback(
    dash.dependencies.Output('map1', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button1', 'n_clicks')])


def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open(r'index1.html',"r", encoding="utf-8").read()

@app.callback(
    dash.dependencies.Output('map2', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button2', 'n_clicks')])


def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open(r'index2.html',"r", encoding="utf-8").read()

#Using the following command we can execute our program
if __name__ == '__main__':
    app.run_server(debug=True)
