#run following command in terminal
python3 -m pip install packaging
python3 -m pip install pandas dash
pip3 install httpx==0.20 dash plotly

# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
   # Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                       encoding = "ISO-8859-1",
                       dtype={'Div1Airport': str, 'Div1TailNum': str, 
                              'Div2Airport': str, 'Div2TailNum': str})
app = dash.Dash(__name__)
app.layout = html.Div(children=[ html.H1('Total number of flights to the destination state split by reporting airline',
                            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                            html.Div(["Input Year: ", dcc. Input(id='input-year',value='2010',
                            type='number', style={'height':'50px', 'font-size': 35}),], 
                            style={'font-size': 40}),html.Br(), html.Br(),
                            html.Div(dcc.Graph(id='bar-plot')),]) 
@app.callback( Output(component_id='bar-plot',component_property='figure'),
             Input(component_id='input-year', component_property='value'))     
def get_graph(entered_year):
        df =  airline_data[airline_data['Year']==int(entered_year)]
        bar_data = df.groupby('DestState')['Flights'].sum().reset_index()
        fig = px.bar(bar_data, x= "DestState", y= "Flights", title='Total number of flights to the destination state split by reporting airline') 
        fig.update_layout(title='Flights to Destination State', xaxis_title='DestState', yaxis_title='Flights')
        return fig    
if __name__ == '__main__':
    app.run_server()    

#to launch aaplication, rum following command in terminal
python3 file_name (here, file name is dash_interactivity.py)


some doubts cleared:
  1. run the required first 3 command in terminal and create new file
  2. to create new file , methos 1 - click on file and choose new file and give a name. method 2- click on explorer icon on left bar, go to project anf coose the first icon shown.
  3. after creating new file, create new terminal.
  4. to launch application, click on skill lab icon on left bar, click on launch icon. put the port number obtained by giving pyhton3 file_name command in terminal
     (note: the last 4 digit is the port number) , and click on launch application
