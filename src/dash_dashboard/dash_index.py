from dash import Dash, html, dcc, callback, Output, Input
from flask_cors import CORS
from ratings_layout import layout as ratings_layout
from years_layout import layout as years_layout
from artists_layout import layout as artists_layout
from styles_layout import layout as styles_layout
from datetime import datetime
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import project_path

#launches the dash app, imports and embeds all the layouts, displaying them in different tabs

with open(project_path+'src/create_csv_dash/etl_date.txt', 'r') as file:
    date_etl = file.readline()

date_time_object = datetime.strptime(date_etl, "%Y-%m-%d %H:%M:%S.%f")
last_date = date_time_object.strftime("%A, %B %d, %Y %H:%M:%S")


external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
app = Dash(
    __name__,
    external_scripts=external_script,
    suppress_callback_exceptions=True
)
app.scripts.config.serve_locally = True
server = app.server


##change the children of the body div according to the tab selected
@callback(
    Output("body", "children"),
    Input("tabs", "value"),
)
def render_content(tab):
    if tab == "tab-1":
        return ratings_layout
    elif tab == "tab-2":
        return artists_layout
    elif tab == "tab-3":
        return years_layout
    elif tab == "tab-4":
        return styles_layout
    else:
        return ratings_layout


app.layout = html.Div([
   ##hdashboard header
    html.Div([
        html.Div([
            html.H1("Your RYS Statistics",className="flex text-2xl w-full items-center text-white font-bold mr-4"),       
            dcc.Tabs(id='tabs', value='tab-1', children=[
                dcc.Tab(label='Ratings', value='tab-1', 
                    className="!bg-[rgb(0,0,0,0)] !text-sm !text-gray-200 !border-0",
                    selected_className="!bg-slate-800 !text-sm !text-white !font-bold !border-2 !border-l-0 !border-white"),                   
                dcc.Tab(label='Artists', value='tab-2',
                    className="!bg-[rgb(0,0,0,0)] !text-sm !text-gray-200 !border-0",
                    selected_className="!bg-slate-800 !text-sm !text-white !font-bold !border-2 !border-l-0 !border-white"), 
                dcc.Tab(label='Years', value='tab-3',
                    className="!bg-[rgb(0,0,0,0)] !text-sm !text-gray-200 !border-0",
                    selected_className="!bg-slate-800 !text-sm !text-white !font-bold !border-2 !border-l-0 !border-white"), 
                dcc.Tab(label='Genres', value='tab-4',
                    className="!bg-[rgb(0,0,0,0)] !text-sm !text-gray-200 !border-0",
                    selected_className="!bg-slate-800 !text-sm !text-white !font-bold !border-2 !border-l-0 !border-r-0 !border-white"), 
            ]),
        ], className="flex w-auto h-auto justify-start"),


        html.Div("Data as of "+last_date,className="w-auto h-auto  text-center text-sm text-gray-50 "),



    ],className="flex justify-between w-full h-auto px-4 items-center mt-1"),

            


    ##dashboard body
    html.Div([],id="body",className="w-full h-full")

],className="flex flex-col w-full h-[850px]")
#bg-gradient-to-br from-red-800 to-blue 


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0") 
